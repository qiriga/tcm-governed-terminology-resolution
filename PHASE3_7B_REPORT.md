# Phase 3.7B local-only release report

## State

**PASS — local-only release QA complete**

Local release preparation and QA were completed without GitHub or other network operations. The sealed test and restricted source material were not accessed.

## Repository checkpoint

- Authenticated GitHub username (author-confirmed; not re-queried): `qiriga`
- Repository URL: `https://github.com/qiriga/tcm-governed-terminology-resolution`
- Current branch: `main`
- Commit: first local release commit to be created after all QA gates pass
- Tracked/staged files: 53
- Remote origin: not configured in local-only mode

## QA results

- Python: 3.12.13 in repository-local isolated `.venv`
- pytest: 8.4.2
- Formal `pytest -q`: PASS — 6 passed, 0 failed in 0.01s
- Release scan: PASS, 0 findings
- SHA-256 manifest: 50 entries, all verified successfully
- Manifest exclusions: `reproducibility/SHA256SUMS` excludes itself to avoid a recursive digest; `PHASE3_7B_REPORT.md` and `reproducibility/release_scan_report.json` are mutable final-QA reports and are intentionally excluded by `scripts/generate_hashes.py`
- `git diff --check`: PASS
- `.venv`: ignored by `.gitignore` and not tracked
- AppleDouble / DS_Store: release-tree artifacts removed; none staged or tracked

## Benchmark release audit

- Total metadata rows: 1,855
- Public benchmark queries: 50 synthetic B4 unsupported queries
- Withheld B1 query strings: 600
- Withheld B2 query strings: 600
- Withheld B3 source-derived query strings: 600
- Withheld real B4 ambiguity queries: 5
- All 1,805 withheld rows have blank query cells
- Complete Latin nomenclature fields and author strings from the terminology resource are absent
- Private mappings are absent
- The sealed test and restricted source material were not accessed and are absent from the release

## Release-file status

- README: finalized with copyright-safe scope, governed A–F logic, evaluation tracks, quick start, tests, benchmark evaluation, figures, metrics, and citation guidance
- LICENSE: finalized as MIT for software only
- DATA_USAGE: finalized with explicit resource and restricted-data exclusions; no CC0 dedication
- CITATION: finalized for version 0.1.0 with the three supplied authors/ORCIDs and repository URL; no DOI invented
- CONTRIBUTING, SECURITY, and RELEASE_METADATA: finalized
- Restricted-content audit: no restricted files identified in the staged file-name review; release scan PASS with zero findings

## Local handoff state

All local QA gates required for the first release commit passed. The first commit is created only after this report, the checksum manifest, checksum verification, release scan, and Git checks are final.

The author may subsequently create the GitHub repository from an authenticated macOS Terminal:

```bash
gh repo create qiriga/tcm-governed-terminology-resolution \
  --public \
  --description "Copyright-safe reproducibility package for a failure-guided reliability study of governed TCM nomenclature resolution." \
  --source . \
  --remote origin
```

Do not push, publish a tag or release, or create a Zenodo DOI until separately authorized.
