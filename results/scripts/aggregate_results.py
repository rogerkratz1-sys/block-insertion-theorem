#!/usr/bin/env python3
import json, csv, glob
from pathlib import Path
in_files = sorted(glob.glob("results/per_run/blocks_index_*.json"))
agg_rows = []
block_agg = {}  # block_size -> [count, contribution_sum]
for p in in_files:
    j = json.load(open(p))
    idx = j.get("index")
    tle = j.get("total_linear_extensions")
    vsum = j.get("verification_sum")
    # block_counts assumed [[count, size], ...] as used earlier
    bc = j.get("block_counts", [])
    bc_summary = ";".join(f"{pair[0]}x{pair[1]}" for pair in bc)
    agg_rows.append({"index": idx, "total_linear_extensions": tle, "verification_sum": vsum, "block_counts_summary": bc_summary})
    for pair in bc:
        count, size = pair[0], pair[1]
        contrib = count * size
        if size not in block_agg:
            block_agg[size] = [0,0]
        block_agg[size][0] += count
        block_agg[size][1] += contrib

# write aggregated_results.csv
with open("results/aggregated_results.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["index","total_linear_extensions","verification_sum","block_counts_summary"])
    writer.writeheader()
    for row in sorted(agg_rows, key=lambda r: int(r["index"])):
        writer.writerow(row)

# write block_size_summary.csv
with open("results/tables/block_size_summary.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["block_size","count","total_contribution"])
    for size in sorted(block_agg.keys()):
        count, contrib = block_agg[size]
        writer.writerow([size, count, contrib])
