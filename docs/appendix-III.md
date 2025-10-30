Appendix III â€” DP aggregation output format, pseudocode, worked traces, and reproducibility notes

Purpose
Suggested text for Appendix III and the repository README: this appendix specifies the exact DP-aggregation output format used to produce BlockSummary artifacts, provides concise pseudocode for DP-aggregation and enumerative routines, includes worked traces that reproduce the dressing-poset block summaries in the paper, and lists reproducibility artifacts and a canonical checklist.
________________________________________
Notation and index convention
â€¢	n = number of elements (vertices).
â€¢	m = number of comparable relations (Hasse edges).
â€¢	Indexing convention: Use 1-based positions in text and human-facing outputs; use 0-based arrays in code only where language-native arrays require it, and document that choice in README and code comments. All BlockSummary examples in this appendix use 1-based positions.
________________________________________
DP aggregation output format (machine- and human-readable)
BlockSummary(index = i) â€” field types
â€¢	index: integer (1-based)
â€¢	total_linear_extensions: integer
â€¢	block_counts: list of [block_size:int, count:int] pairs where block_size â‰¥ 1
â€¢	contributions: list of [block_size:int, count:int, contribution:int] triples with contribution = block_size * count
â€¢	verification_sum: integer (sum of contributions; must equal total_linear_extensions)
Example JSON (write this exact content to disk):
{
  "index": 5,
  "total_linear_extensions": 734,
  "block_counts": [[2,40],[3,62],[4,72],[5,36]],
  "contributions": [[2,40,80],[3,62,186],[4,72,288],[5,36,180]],
  "verification_sum": 734
}
Example CSV rows (one row per (index, block_size); header included):
index,block_size,block_count,contribution,total_linear_extensions
5,2,40,80,734
5,3,62,186,734
5,4,72,288,734
5,5,36,180,734
Tiny interpretation table (for readers)
â€¢	block_size = number of absolute slots that element i may occupy in a full extension when that reduced-permutation class occurs.
â€¢	count = number of reduced permutations (linear extensions of P \ {i}) producing that block_size.
â€¢	contribution = block_size Ã— count; summing contributions across block_sizes yields total_linear_extensions for index i.
________________________________________
Pseudocode
Notes:
â€¢	P \ {i} denotes the poset with element i removed.
â€¢	A reduced permutation is a linear extension of P \ {i}.
â€¢	The DP-aggregation routine compresses many reduced permutations that share identical p and s-derived block sizes into aggregated counts.
Enumerative backtracking to generate reduced permutations (conceptual, reference implementation):
function enumerate_reduced_extensions(poset_minus_i):
  results = []
  backtrack(current = empty_list, available = all_elements_of(poset_minus_i))
  return results

function backtrack(current, available):
  if available is empty:
    append copy(current) to results
    return
  for x in available such that all predecessors_of(x) are in current:
    remove x from available
    append x to current
    backtrack(current, available)
    pop current
    add x back to available
Compute p, s, k and update block summary for a single reduced permutation:
function process_reduced_permutation(R, poset, i, block_counts):
  # R is a reduced permutation: list of elements in P \ {i} in order
  p = index_of_last_forced_predecessor(R, i, poset)  # 0 if none (1-based positions)
  s = index_of_first_forced_successor(R, i, poset)   # len(R)+1 if none
  k = (s - p - 1)
  block_size = k + 1
  block_counts[block_size] += 1
DP-aggregation (bitmask/subset-DP sketch; adapt to chosen implementation):
function dp_aggregate(poset_minus_i):
  # choose state_signature that preserves enough info to derive p,s at the end
  initialize dp_map: mapping from state_signature -> count
  dp_map[initial_signature] = 1
  while not all elements placed:
    new_dp_map = empty mapping
    for signature, count in dp_map:
      for choice in available_choices_for(signature):
        new_signature = update_signature(signature, choice)
        new_dp_map[new_signature] += count
    dp_map = new_dp_map
  # convert final DP classes into block_counts by deriving p,s,k per class
  block_counts = empty map
  for signature, count in dp_map:
    p, s = p_s_from_signature(signature, poset, i)  # compute directly if possible
    k = (s - p - 1)
    block_counts[k+1] += count
  return block_counts
Implementation notes
â€¢	The key compression decision is the design of state_signature: it must preserve exactly the information needed to compute p and s for final classes, and no more. Document the chosen signature format in the README.
â€¢	For correctness-first development, run the enumerator to produce ground truth block_counts for small instances; use those results to refine state_signature choices.
â€¢	Precompute transitive-closure/reachability once and reuse results to compute forced predecessors/successors cheaply.
â€¢	Include unit tests that compare dp_aggregate output to enumerate_reduced_extensions + process_reduced_permutation for small instances.
________________________________________


Worked traces that reproduce the dressing-poset block summaries
Dressing-poset cover relations (for reference): (1,2), (3,2), (4,3), (3,5), (6,5), (6,7), (6,8). Total linear extensions = 734.
Note: the single â€œRepresentative reduced permutationâ€ shown below is an example illustrating how p and s are computed; aggregated block_counts are obtained by repeating process_reduced_permutation over all reduced permutations of P \ {i}.
Worked trace for index = 1 (socks)
Representative reduced permutation: R = [3,4,5,6,7,8,2] # permutation of P \ {1}
1.	forced predecessors of 1 in R: none â‡’ p = 0
2.	forced successors of 1 in R: {2} occurs at position 7 in R â‡’ s = 7
3.	incomparable block positions p+1..sâˆ’1 = 1..6 â†’ elements [3,4,5,6,7,8] â‡’ k = 6
4.	block_size = k+1 = 7 â†’ increment block_counts[7] by 1 â†’ contribution +7
Repeat for all reduced permutations; final aggregated block_counts (index = 1):
â€¢	block_size 3: count 6 â†’ contribution 18
â€¢	block_size 4: count 18 â†’ contribution 72
â€¢	block_size 5: count 30 â†’ contribution 150
â€¢	block_size 6: count 38 â†’ contribution 228
â€¢	block_size 7: count 38 â†’ contribution 266
verification_sum = 18 + 72 + 150 + 228 + 266 = 734
Full block summary JSON for index = 1:
{
  "index": 1,
  "total_linear_extensions": 734,
  "block_counts": [[3,6],[4,18],[5,30],[6,38],[7,38]],
  "contributions": [[3,6,18],[4,18,72],[5,30,150],[6,38,228],[7,38,266]],
  "verification_sum": 734
}
Worked trace for index = 5 (belt)
Representative reduced permutation: R = [4,1,3,2,6,7,8] # permutation of P \ {5}
1.	forced predecessors of 5: {3,6} appear at positions 3 and 5 in R â‡’ p = 5
2.	forced successors of 5: none â‡’ s = len(R)+1 = 8
3.	incomparable block positions p+1..sâˆ’1 = 6..7 â†’ elements [7,8] â‡’ k = 2
4.	block_size = k+1 = 3 â†’ increment block_counts[3] by 1 â†’ contribution +3
Final aggregated block_counts (index = 5):
â€¢	block_size 2: count 40 â†’ contribution 80
â€¢	block_size 3: count 62 â†’ contribution 186
â€¢	block_size 4: count 72 â†’ contribution 288
â€¢	block_size 5: count 36 â†’ contribution 180
verification_sum = 80 + 186 + 288 + 180 = 734
Full block summary JSON for index = 5:
{
  "index": 5,
  "total_linear_extensions": 734,
  "block_counts": [[2,40],[3,62],[4,72],[5,36]],
  "contributions": [[2,40,80],[3,62,186],[4,72,288],[5,36,180]],
  "verification_sum": 734
}
________________________________________
Reproducibility artifacts and canonical checklist (to include in repo README and release metadata)
Repository placeholder (insert when available): [repository URL to be inserted]
Required repository contents
â€¢	Source code: 
o	enumerative backtracker (reference implementation)
o	DP-aggregation implementation (bitmask/subset-DP or compressed-state DP)
o	scripts that produce BlockSummary JSON and CSV outputs for every index
â€¢	Input files: 
o	poset files (adjacency-list format) for all instances used in the paper (including dressing_poset.adj)
o	optional: explicit lists of reduced permutations used in worked traces
â€¢	Example outputs: 
o	BlockSummary JSON files for each index of each instance
o	CSV summary files for plotting and tables
â€¢	Experiment logs: 
o	run commands with timestamps, environment details, measured runtimes, and peak memory
â€¢	README: 
o	instructions for reproducing the dressing-poset block summaries and running DP aggregation on additional instances
Canonical reproducibility checklist (copy this into the repository README and release notes)
1.	Code commit hash or DOI for the exact code version used in experiments.
2.	Exact command lines used for each run (examples below).
3.	Input poset files (adjacency-list format) used to produce paper results.
4.	Output JSON/CSV files containing BlockSummary entries that match paper tables/figures.
5.	Software environment and hardware: language/runtime and version, OS, CPU model, cores, RAM, and any non-default compilation flags.
Example command lines (illustrative; copy-and-paste ready)
# Enumerate reduced permutations and produce block summary for index=1
./enumerate_reduced --poset dressing_poset.adj --index 1 --out blocks_index_1.json

# Run DP aggregation for all indices
./dp_aggregate --poset dressing_poset.adj --out block_summaries_all.json

# Verify produced verification_sum equals total linear extensions
python verify_block_summaries.py block_summaries_all.json  # exits 0 on success, nonzero on mismatch
Maintenance note for authors and reproducibility officers: copy this canonical checklist verbatim into the repository README and into the release tag/changelog for the submission used in the paper; include the code commit hash/DOI and the path or URL of example outputs so reviewers can run verification commands without additional setup.
________________________________________
Minimal notes on format conventions and naming
Indexing
â€¢	Human-facing tables and figures use 1-based positions.
â€¢	Machine-readable JSON and CSV files use the documented indexing in the repository README and schema.
Required field names (use these exact keys)
â€¢	total_linear_extensions, block_counts, contributions, verification_sum, per_run_file, wall_seconds, cpu_seconds, peak_mem_mb, seed, repeat, exit_code, notes, commit_hash, host.
Repository artifacts referenced in this appendix
â€¢	results/aggregated_results.csv
â€¢	results/per_run/*.json (BlockSummary JSONs per Appendix III schema)
â€¢	results/logs/*.log and *.time.txt
â€¢	results/plots/*.(png|pdf) (high-resolution raster and vector versions)
â€¢	results/tables/*.csv (numeric summaries)
â€¢	results/scripts/*.py (aggregation, verification, plotting scripts)
â€¢	metadata/commit_hash.txt, metadata/checksums.txt, run_manifest.txt, CITATION.
Quick reviewer checks (cut and paste)
â€¢	python3 scripts/verify_block_summaries.py results/per_run/*.json
â€¢	python3 scripts/aggregate_results.py --input results/per_run/ --out results/aggregated_results.csv
â€¢	sha256sum -c metadata/checksums.txt
Access and provenance
â€¢	Repository URL/DOI, exact commit hash, and access status are recorded in metadata/commit_hash.txt. Reviewers should use those identifiers to retrieve the archival snapshot referenced in this appendix.
Notes on verification and machine readability
â€¢	BlockSummary JSON files conform to the schema given in Appendix III; verify_block_summaries.py validates verification_sum against total_linear_extensions and exits nonzero on mismatches.
â€¢	aggregated_results.csv contains one row per run and includes a per_run_file column linking each row to its BlockSummary JSON for traceability.
________________________________________
Implementation Notes
Full runnable Python source files implementing the experiments are available in the project repository; Appendix IV records the repository URL/DOI and commit hash used to produce the results.










<!-- appended-for-normalization -->
