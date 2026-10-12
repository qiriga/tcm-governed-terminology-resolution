# Phase 3.7A release-staging report

## Outcome

An independent, copyright-safe staging repository was assembled around governed terminology resolution. No remote is configured, and no publication action was taken.

## Public candidate files

The candidate contains cleaned resolver modules, CLI evaluation and release-verification utilities, a schema, anonymous benchmark metadata, a blank public KB stub, synthetic toy fixtures, frozen aggregate metrics, tests, figures, source aggregates, and repository governance files.

## Excluded private material

Restricted evaluation assets, complete KB content, complete Latin and attribution fields, source-resource documents/tables, private identifier crosswalks, complete alias collections, model assets, credentials, internal notes, reviewer simulations, and manuscript working history were not staged.

## Benchmark release status

- B1: `AUTHOR_REVIEW`; query text withheld.
- B2: `AUTHOR_REVIEW`; query text withheld.
- B3: `AUTHOR_REVIEW`; source-derived perturbation text withheld pending rights review.
- B4: 50 synthetic unknowns are `PUBLIC_SAFE`; five source-based ambiguity rows are `AUTHOR_REVIEW` with query text withheld.

## Interpretation

Expected metrics describe the frozen covered-resource benchmark, not unseen generalization. The public runnable path demonstrates record-resolution behavior without factual Latin target fields.

## Readiness gates

The five pytest modules are present. No isolated environment containing pytest was available, so pytest was not installed or downloaded during recovery. Six test functions previously passed through a dependency-free local runner; the toy workflow, repeatability check, and figure-input verification also passed. The final release scan and SHA-256 manifest were regenerated after staging fixes.

Git was initialized locally with no remote. The staging repository is **READY_FOR_AUTHOR_RELEASE_REVIEW**, not approved for public release. Publication still requires the decisions in `RELEASE_REVIEW.md`, execution of pytest after installing the declared local test dependency, activation of a code license, a final repository URL, and manual pre-publication review.

## Final QA summary

- Benchmark rows: 1,855 total (B1 600; B2 600; B3 600; B4 55).
- Release status: 1,805 `AUTHOR_REVIEW`; 50 `PUBLIC_SAFE` synthetic B4 unsupported queries.
- Query exposure: only the 50 `PUBLIC_SAFE` synthetic B4 rows contain query text.
- Latin target-field headers: none.
- Git remote: none.
- Release scan: PASS with zero findings.
- SHA-256 manifest: present under `reproducibility/`.

## Commands to run only after author approval

```bash
git add .
git commit -m "Release copyright-safe reproducibility package"
git branch -M main
git remote add origin https://github.com/<ORG>/tcm-governed-terminology-resolution.git
git push -u origin main
```

The hosting repository must be created manually first. Replace `<ORG>` and update `CITATION.cff`; do not run these commands until all release decisions are resolved.
