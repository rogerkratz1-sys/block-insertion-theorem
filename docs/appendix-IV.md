Appendix IV â€” Full empirical results, plots, and logs
Implementation notes
Appendix IV contains the reproducibility bundle: aggregated results, per run BlockSummary JSONs, raw logs, high resolution plots, and the runnable Python scripts and auxiliary source files used to generate all tables and figures. The repository URL/DOI and exact commit hash used to produce these artifacts are recorded in metadata/commit_hash.txt and summarized below.
Repository snapshot (placeholder â€” replace before submission)
Repository URL/DOI: 
Commit: 
Access: <public | private-under-review | embargoed until YYYY-MM-DD>
CITATION: CITATION file included in the repository describing how to cite the code and DOI.
Purpose
Archive and describe the complete empirical artifacts produced for the paper: aggregated numeric tables, all runtime/memory logs, generated plot files used in the manuscript, and auxiliary scripts for reproducing and browsing results. Use this appendix as the canonical index of files to include in the supplementary repository and in any archival snapshot (DOI).
________________________________________
Contents (recommended file layout in the repository)
â€¢	results/ 
o	aggregated_results.csv
o	per_run/ 
ï‚§	dressing_poset_enum.json
ï‚§	dressing_poset_bit_enum.json
ï‚§	dressing_poset_dp.json
ï‚§	dressing_poset_bit_dp.json
ï‚§	dressing_poset_sampler_rep1.json ... dressing_poset_sampler_repN.json
ï‚§	chain_n10_enum.json, chain_n10_bit_dp.json, ...
o	logs/ 
ï‚§	dressing_poset_enum.log
ï‚§	dressing_poset_enum.time.txt (output from /usr/bin/time -v)
ï‚§	chain_n20_dp.log
ï‚§	...
o	plots/ 
ï‚§	runtime_vs_n.png; runtime_vs_n.pdf
ï‚§	memory_vs_n.png; memory_vs_n.pdf
ï‚§	sampler_error_vs_time.png; sampler_error_vs_time.pdf
o	tables/ 
ï‚§	runtime_table_by_instance.csv
ï‚§	memory_table_by_instance.csv
ï‚§	sampler_summary.csv
o	scripts/ 
ï‚§	aggregate_results.py
ï‚§	plot_runtimes.py
ï‚§	verify_block_summaries.py
o	metadata/ 
ï‚§	commit_hash.txt
ï‚§	environment.yml or requirements.txt
ï‚§	hardware.txt
ï‚§	run_manifest.txt (list of every run and exact command line)
ï‚§	checksums.txt (SHA256 checksums for large files)
ï‚§	CITATION
Include the full directory tree above in the repository release used for paper evaluation.
________________________________________
File format and required fields
â€¢	aggregated_results.csv (one row per run) â€” required columns: instance, n, algo, variant, wall_seconds, cpu_seconds, peak_mem_mb, total_linear_extensions, verification_sum, seed, repeat, exit_code, notes, commit_hash, host, per_run_file.
â€¢	BlockSummary JSON files â€” follow the Appendix III schema exactly (index, total_linear_extensions, block_counts, contributions, verification_sum).
â€¢	Logs â€” plain text; include tool stdout/stderr and instrumentation from /usr/bin/time -v or equivalent.
â€¢	Plots â€” provide high resolution PNG and vector PDF versions for each figure referenced in the paper.
â€¢	Metadata files â€” record environment and hardware (CPU model, cores, RAM, OS, Python/R/compiled binary versions), the commit hash used to produce results, DOI, and checksums.
________________________________________
Mandatory verification steps included in the archive
1.	verify_block_summaries.py checks each BlockSummary JSON in results/per_run/ and exits 0 if all verification_sum == total_linear_extensions; otherwise prints mismatches and exits nonzero.
2.	aggregate_results.py consolidates per_run JSONs into results/aggregated_results.csv and regenerates CSV tables in results/tables/. Include example invocation in run_manifest.txt.
Quick reviewer check (cut-and-paste commands)
python3 scripts/verify_block_summaries.py results/per_run/*.json
python3 scripts/aggregate_results.py --input results/per_run/ --out results/aggregated_results.csv
sha256sum -c metadata/checksums.txt
Example invocations to include in run_manifest.txt
python3 scripts/verify_block_summaries.py results/per_run/*.json
python3 scripts/aggregate_results.py --input results/per_run/ --out results/aggregated_results.csv
python3 scripts/plot_runtimes.py --input results/tables/runtime_table_by_instance.csv --out results/plots/runtime_vs_n.png
________________________________________
Plot descriptions (link each plot to the corresponding CSV/table)
â€¢	runtime_vs_n.(png|pdf): median wall clock time vs n (log scale). Data source: runtime_table_by_instance.csv (median across repeats).
â€¢	memory_vs_n.(png|pdf): median peak_mem_mb vs n (log scale). Data source: memory_table_by_instance.csv.
â€¢	sampler_error_vs_time.(png|pdf): sampler estimator error (or std) vs wall_seconds for Sampler and BIT+Sampler. Data source: sampler_summary.csv.
Add captions and figure numbers in the repository README or in the paperâ€™s figure list that match these filenames.
________________________________________
Large tables and numeric summaries
Provide CSVs in results/tables/ with the following conventions:
â€¢	runtime_table_by_instance.csv: columns instance, n, algo, median_wall_seconds, mean_wall_seconds, sd_wall_seconds, median_peak_mem_mb, mean_peak_mem_mb, sd_peak_mem_mb, success_rate, per_run_file_examples.
â€¢	sampler_summary.csv: columns instance, algo, repeat, seed, wall_seconds, mean_estimate, std_error, ess, notes, per_run_file.
Link each table row to the per run JSON filename in a per_run_file column so reviewers can inspect raw artifacts.
________________________________________
Storage, archival, and citation
â€¢	Produce a release tag in the code repository and mint a DOI (e.g., via Zenodo) for the exact release used to generate Appendix IV artifacts. Store the DOI and the commit hash in metadata/commit_hash.txt.
â€¢	Include checksums (SHA256) for all large files (plots, aggregated CSVs) in metadata/checksums.txt so reviewers can verify download integrity.
Example metadata/commit_hash.txt:
commit: 6a1b2c3d4e5f67890abcdef1234567890abcdef12
doi: 10.5281/zenodo.xxxxxxxx
date: 2025-10-22
CITATION file (required)
Provide a short CITATION file describing how to cite the repository and DOI.
________________________________________

Repository snapshot: Repository URL: https://github.com/rogerkratz1-sys/block-insertion-theorem.git; DOI: 10.5281/zenodo.17451500

Repository snapshot: https://github.com/rogerkratz1-sys/block-insertion-theorem.git; DOI: 10.5281/zenodo.17451500; Commit: d65b6554682e637bedbcf916f26495867e00dc18; Access: public; v1.0.0; archived 2025-10-26

Verification
To reproduce this snapshot:
git clone https://github.com/rogerkratz1-sys/block-insertion-theorem.git
git checkout d65b6554682e637bedbcf916f26495867e00dc18

License: MIT
Contact: Roger Kratz <rogerkratz1@gmail.com> or open an issue at https://github.com/rogerkratz1-sys/block-insertion-theorem/issues
Checksums (SHA256):
  docs/appendix-III.docx: 6EA6FC26A41EBFF431EBAF8DF1626370F17EAA7C61935797C43C60CF74613F02
  docs/appendix-IV.docx: 0A1BB3E483AE4412E9E2B30BA7AE75CBCC6689B9B40D6152A9830D42879C728E

