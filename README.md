# TCM Governed Terminology Resolution

Copyright-safe reproducibility package for the paper:

> **From Generative Fine-Tuning to Governed Terminology Resolution: A Reliability Study of Traditional Chinese Medicine Nomenclature Mapping**

This package reproduces the governed record-resolution logic, evaluation tooling, synthetic examples, figures, and aggregate expected metrics used to study a failure-guided reformulation of terminology mapping. It does not reproduce the full LoRA or generative fine-tuning study.

## Scope and data boundary

The package does **not** redistribute the copyrighted terminology resource, complete Latin nomenclature fields, author strings, private mappings, the full knowledge base, source PDFs or spreadsheets, training data, model artifacts, or the sealed generalization test set.

The public benchmark retains 50 synthetic B4 unsupported queries. B1, B2, and source-derived B3 query strings and five real B4 ambiguity queries are withheld; their public metadata cannot reconstruct the source content. See `DATA_USAGE.md` for the governing terms.

## Failure-guided task reformulation

The study reframes unconstrained string generation as governed record resolution. Deterministic evidence may bind a query to a known record; approximate similarity may retrieve candidates but cannot itself emit a factual resolution. Ambiguous and unsupported inputs are routed to review or abstention, with provenance recorded for every automatic decision.

## Governed Levels A–F

- **Level A:** unique exact main-key match may auto-resolve.
- **Level B:** unique verified-alias match may auto-resolve.
- **Level C:** unique normalized deterministic match may auto-resolve.
- **Level D:** fuzzy retrieval supplies candidates only and never binds a factual result.
- **Level E:** ambiguous input routes to review or abstention.
- **Level F:** unsupported input routes to review or abstention.

Only a unique eligible Level A, B, or C record can cross the factual-binding boundary.

## Evaluation tracks

The **covered-resource track** evaluates resolution behavior where the governed resource defines the candidate space. Its benchmark results are not unseen-generalization metrics.

The distinct **generalization track** concerns unseen mappings. Its sealed test set is not included, and this repository makes no claim to reproduce that sealed evaluation.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
pytest -q
```

Run the synthetic demonstration:

```bash
python scripts/run_benchmark.py \
  --kb data/toy_kb.csv \
  --benchmark examples/toy_benchmark.csv \
  --output examples/toy_predictions.csv
python scripts/evaluate_benchmark.py \
  --benchmark examples/toy_benchmark.csv \
  --predictions examples/toy_predictions.csv
python scripts/repeatability_audit.py \
  --first examples/toy_predictions.csv \
  --second examples/toy_predictions.csv
python scripts/verify_release.py
```

## Benchmark evaluation and expected metrics

`data/public_benchmark_candidate.csv` implements the public schema in `data/benchmark_schema.json`. Only the 50 `PUBLIC_SAFE` synthetic B4 rows contain runnable public queries. The frozen aggregate paper results are in `data/expected_metrics.json`; they describe the covered-resource benchmark and must not be interpreted as unseen generalization. Toy outputs are demonstrations, not paper results.

## Figures

Figures 1–3 are provided in PDF, PNG, and SVG under `figures/`. `figures/source_data.json` and `scripts/generate_figures.py` support their public-safe reproduction.

## Citation

Please cite the software package using `CITATION.cff` and cite the accompanying paper by its title above. No paper DOI is asserted here.

## License

The MIT License applies to software only. Data and terminology-resource exclusions are described in `DATA_USAGE.md`.
