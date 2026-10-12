#!/usr/bin/env python3
"""Generate the public-candidate SHA-256 manifest."""
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "reproducibility" / "SHA256SUMS"
MUTABLE_REPORTS = {
    ROOT / "PHASE3_7B_REPORT.md",
    ROOT / "reproducibility" / "release_scan_report.json",
}


def main() -> None:
    lines = []
    for path in sorted(ROOT.rglob("*")):
        if (
            not path.is_file()
            or ".git" in path.parts
            or ".venv" in path.parts
            or path == OUTPUT
            or path in MUTABLE_REPORTS
            or path.name.startswith("._")
        ):
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        lines.append(f"{digest}  {path.relative_to(ROOT)}")
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(lines)} hashes to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
