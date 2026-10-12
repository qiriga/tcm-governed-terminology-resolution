#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REPORT=ROOT/"reproducibility"/"release_scan_report.json"
TEXT_SUFFIXES={".md",".py",".json",".csv",".toml",".txt",".cff",".gitignore",""}
FORBIDDEN=["test"+"_locked", "known"+"_terms_db", "private"+"_target", "/"+"Volumes"+"/", "API"+"_KEY", "TO"+"KEN", "SE"+"CRET", "pass"+"word", "terminology"+"_records.jsonl", "full"+"_latin_name", "source"+"_page_or_evidence"]
SKIP={REPORT.resolve()}
def main():
    findings=[]; scanned=0
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts or ".venv" in path.parts or path.name.startswith("._") or path.resolve() in SKIP: continue
        scanned += 1
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {"LICENSE","CITATION.cff"}: continue
        try: text=path.read_text(encoding="utf-8")
        except UnicodeDecodeError: continue
        lower=text.lower()
        for term in FORBIDDEN:
            if term.lower() in lower: findings.append({"file":str(path.relative_to(ROOT)),"rule":term})
    result={"status":"FAIL" if findings else "PASS","files_scanned":scanned,"findings":findings,"scope":"staging repository; version-control internals excluded"}
    REPORT.parent.mkdir(parents=True, exist_ok=True); REPORT.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2)); raise SystemExit(1 if findings else 0)
if __name__ == "__main__": main()
