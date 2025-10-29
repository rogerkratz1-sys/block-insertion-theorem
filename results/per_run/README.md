Per-run BlockSummary JSON files.
Filename pattern: blocks_index_<i>.json

Schema highlights:
- index: integer
- instance: string
- n: integer
- algo: string
- target: integer (optional)
- counts_by_block_size: object mapping block_size (string) -> count (int)
- total_orderings: integer
- verification_sum: integer
- command: string
- wall_seconds, cpu_seconds: numeric
- peak_mem_mb: numeric or null
- host: string
- commit_hash: short git hash recording code provenance
- notes: free-form string

Place small JSONs here. For large outputs, record checksums in metadata/checksums.txt and keep large binaries out of the repo.
