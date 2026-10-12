#!/usr/bin/env python3
"""Validate frozen public figure inputs and report the supplied publication assets.

The final vector/raster artwork is versioned in figures/. Regeneration requires the
authors' typesetting toolchain; this script verifies that its public aggregate inputs
and expected assets are present without accessing row-level study data.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/"figures"/"source_data.json").read_text(encoding="utf-8"))
assert data["covered_resource"]["total"] == 1855
assert data["covered_resource"]["automatic_resolutions"] + data["covered_resource"]["review_or_abstention"] == 1855
assert data["covered_resource"]["correct_automatic_resolutions"] + data["covered_resource"]["unsafe_automatic_resolutions"] == 1403
for number in (1,2,3):
    matches=list((ROOT/"figures").glob(f"Fig{number}_*.pdf"))+list((ROOT/"figures").glob(f"Fig{number}_*.png"))+list((ROOT/"figures").glob(f"Fig{number}_*.svg"))
    assert len(matches)==3, f"Figure {number} requires SVG, PDF, and PNG"
print("Figure assets and frozen aggregate source data verified.")
