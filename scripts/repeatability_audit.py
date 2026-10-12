#!/usr/bin/env python3
import argparse, csv, json
from pathlib import Path
def read(path):
    with Path(path).open(encoding="utf-8", newline="") as handle: return {r["benchmark_id"]:r for r in csv.DictReader(handle)}
def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--first", required=True); parser.add_argument("--second", required=True); args=parser.parse_args(); a,b=read(args.first),read(args.second)
    if set(a)!=set(b): raise ValueError("prediction ID sets differ")
    fields=("predicted_action","predicted_public_record_id","candidate_public_record_ids","resolution_level"); same=sum(all(a[k].get(f,"")==b[k].get(f,"") for f in fields) for k in a)
    print(json.dumps({"repeatability":{"numerator":same,"denominator":len(a),"value":same/len(a) if a else None}}, indent=2))
if __name__ == "__main__": main()
