# block-insertion-theorem
Algorithms, examples, and implementation notes for the Block Insertion Theorem, including applications to poset enumeration and runtime analysis.
### Project Overview
Algorithms, examples, and implementation notes for the Block Insertion Theorem with worked traces, reproducible code, and empirical artifacts for poset enumeration, DP aggregation, and sampler evaluation.

---

### Repository Contents
- **src/**: reference implementations  
  - enumerative backtracker; DP aggregation (bitmask and compressed-state variants); samplers and utilities
- **data/**: input poset files in adjacency-list format  
  - **dressing_poset.adj** and other instances used in the paper
- **results/**: reproducibility bundle described in Appendix IV  
  - **per_run/**: BlockSummary JSONs and per-run logs  
  - **aggregated_results.csv**, **plots/**, **tables/**  
  - **metadata/**: commit_hash.txt, checksums.txt, hardware.txt, run_manifest.txt
- **scripts/**: helper scripts  
  - **verify_block_summaries.py**, **aggregate_results.py**, **plot_runtimes.py**
- **docs/**: appendices, worked traces, and manuscript supplements
- **CITATION**: how to cite this repository and DOI
- **LICENSE**: project license

---

### Quickstart
1. Clone repository and enter directory:
   ```bash
   git clone <REPOSITORY_URL> && cd block-insertion-theorem
