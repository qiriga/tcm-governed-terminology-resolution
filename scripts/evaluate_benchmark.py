#!/usr/bin/env python3
import argparse, csv, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from tcm_resolution.metrics import evaluate_rows
def read(path):
    with Path(path).open(encoding="utf-8", newline="") as handle: return list(csv.DictReader(handle))
def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--benchmark", required=True); parser.add_argument("--predictions", required=True); args=parser.parse_args(); print(json.dumps(evaluate_rows(read(args.benchmark), read(args.predictions)), indent=2))
if __name__ == "__main__": main()
