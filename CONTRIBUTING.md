# Contributing

Open an issue before proposing behavioral changes. Changes must preserve the A–F decision semantics, keep Level D candidate-only and nonbinding, and use only synthetic or otherwise public-safe fixtures.

Never submit terminology-resource assets, complete Latin fields, author strings, identifier crosswalks, source-derived restricted queries, sealed-test content, training data, model artifacts, private manuscript history, or confidential material.

Before a pull request, run:

```bash
pytest -q
python scripts/verify_release.py
git diff --check
```
