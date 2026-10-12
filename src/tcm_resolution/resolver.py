from __future__ import annotations
from dataclasses import dataclass
from .decision_levels import DecisionLevel, may_emit_factual_binding
from .normalization import normalize_key
from .provenance import ProvenanceTrace
from .retrieval import rank_candidates

@dataclass(frozen=True)
class PublicRecord:
    public_record_id: str
    canonical_query_key: str
    verified_aliases: tuple[str, ...] = ()
    ambiguity_status: str = "UNAMBIGUOUS"
    review_required: bool = False

    @property
    def eligible(self) -> bool:
        return self.ambiguity_status == "UNAMBIGUOUS" and not self.review_required

@dataclass(frozen=True)
class Resolution:
    resolution_level: str
    predicted_action: str
    predicted_public_record_id: str | None
    candidate_public_record_ids: tuple[str, ...]
    match_method: str
    retrieval_score: float | None
    provenance: dict

class GovernedResolver:
    def __init__(self, records: list[PublicRecord], fuzzy_threshold: float = 0.5):
        self.records = {r.public_record_id: r for r in records}
        self.fuzzy_threshold = fuzzy_threshold
        self.main, self.alias, self.normalized, self.names = {}, {}, {}, {}
        for record in records:
            rid = record.public_record_id
            self.main.setdefault(record.canonical_query_key, []).append(rid)
            strings = [record.canonical_query_key, *record.verified_aliases]
            self.names[rid] = sorted({normalize_key(value) for value in strings})
            for value in record.verified_aliases:
                self.alias.setdefault(value, []).append(rid)
            for value in strings:
                self.normalized.setdefault(normalize_key(value), set()).add(rid)
        self.main = {k: sorted(set(v)) for k, v in self.main.items()}
        self.alias = {k: sorted(set(v)) for k, v in self.alias.items()}
        self.normalized = {k: sorted(v) for k, v in self.normalized.items()}

    def _deterministic(self, level, method, ids):
        eligible = [rid for rid in sorted(set(ids)) if self.records[rid].eligible]
        if may_emit_factual_binding(level, len(eligible)) and len(ids) == 1:
            rid = eligible[0]
            trace = ProvenanceTrace(rid, level.value, method).as_dict()
            return Resolution(level.value, "AUTO_RESOLVE", rid, (), method, None, trace)
        trace = ProvenanceTrace(None, DecisionLevel.E.value, method).as_dict()
        return Resolution(DecisionLevel.E.value, "REVIEW", None, tuple(sorted(set(ids))), method, None, trace)

    def resolve(self, query: str) -> Resolution:
        ids = self.main.get(query, [])
        if ids:
            return self._deterministic(DecisionLevel.A, "exact_main_name", ids)
        ids = self.alias.get(query, [])
        if ids:
            return self._deterministic(DecisionLevel.B, "verified_alias", ids)
        ids = self.normalized.get(normalize_key(query), [])
        if ids:
            return self._deterministic(DecisionLevel.C, "normalized_deterministic", ids)
        ranked = rank_candidates(query, self.names)
        top = ranked[0][0] if ranked else 0.0
        if top < self.fuzzy_threshold:
            trace = ProvenanceTrace(None, DecisionLevel.F.value, "fuzzy_below_threshold").as_dict()
            return Resolution(DecisionLevel.F.value, "ABSTAIN", None, (), "fuzzy_below_threshold", round(top, 12), trace)
        candidates = tuple(rid for _, rid in ranked)
        trace = ProvenanceTrace(None, DecisionLevel.D.value, "fuzzy_candidate_retrieval").as_dict()
        return Resolution(DecisionLevel.D.value, "REVIEW", None, candidates, "fuzzy_candidate_retrieval", round(top, 12), trace)
