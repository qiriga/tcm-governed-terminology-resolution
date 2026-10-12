#!/usr/bin/env python3
import argparse, csv, sys
from dataclasses import asdict
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from tcm_resolution import GovernedResolver, PublicRecord

def truth(value): return str(value).strip().lower() == "true"
def read(path):
    with Path(path).open(encoding="utf-8", newline="") as handle: return list(csv.DictReader(handle))
def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--kb", required=True); parser.add_argument("--benchmark", required=True); parser.add_argument("--output", required=True); args = parser.parse_args()
    records=[]
    for row in read(args.kb):
        records.append(PublicRecord(row["public_record_id"], row["canonical_query_key"], tuple(x for x in row.get("verified_aliases", "").split("|") if x), row.get("ambiguity_status", "UNAMBIGUOUS"), truth(row.get("review_required", "false"))))
    resolver=GovernedResolver(records); rows=[]
    for item in read(args.benchmark):
        if not item.get("query"): continue
        result=resolver.resolve(item["query"])
        rows.append({"benchmark_id":item["benchmark_id"],"predicted_action":result.predicted_action,"predicted_public_record_id":result.predicted_public_record_id or "","candidate_public_record_ids":"|".join(result.candidate_public_record_ids),"resolution_level":result.resolution_level})
    out=Path(args.output); out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as handle:
        writer=csv.DictWriter(handle, fieldnames=rows[0].keys() if rows else ["benchmark_id","predicted_action","predicted_public_record_id","candidate_public_record_ids","resolution_level"]); writer.writeheader(); writer.writerows(rows)
if __name__ == "__main__": main()
