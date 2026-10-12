from __future__ import annotations
from dataclasses import asdict, dataclass

@dataclass(frozen=True)
class ProvenanceTrace:
    public_record_id: str | None
    resolution_level: str
    match_method: str
    kb_traceable: bool = True

    def as_dict(self) -> dict:
        return asdict(self)
