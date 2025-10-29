#!/usr/bin/env python3
# index1_blocksize_dp_poset_n8.py
#
# Enumerate all U-extensions (U = V \ {target}); for each U-ordering try every insertion
# position for target and accept it only if the resulting full ordering satisfies all
# precedence constraints. Tally counts_U[slots] = number of distinct U-orderings with
# exactly 'slots' valid insertion positions. Print block-size distribution and invariant total.

from collections import defaultdict
from typing import List, Dict, Set

# Poset given by cover relations on 1..8
covers: Dict[int, List[int]] = {
    1: [2],
    2: [],
    3: [2, 5],
    4: [3],
    5: [],
    6: [5, 7, 8],
    7: [],
    8: []
}

V = list(range(1, 9))

# Build immediate predecessors
preds: Dict[int, List[int]] = {v: [] for v in V}
for u, ws in covers.items():
    for w in ws:
        preds[w].append(u)

# Ensure all keys exist
for v in V:
    covers.setdefault(v, [])
    preds.setdefault(v, [])

# Helper: check that a full ordering 'ordering' is a linear extension
def is_valid_full_order(ordering: List[int]) -> bool:
    pos = {v: i for i, v in enumerate(ordering)}
    for u, ws in covers.items():
        for w in ws:
            if pos[u] >= pos[w]:
                return False
    return True

# Choose target
target = 1
U = [v for v in V if v != target]

# Build indegree inside U (count only immediate predecessors that lie in U)
pred_U = {u: [p for p in preds[u] if p in U] for u in U}
initial_indeg = {u: len(pred_U[u]) for u in U}

# Backtrack to enumerate all U-extensions; for each U-ordering count valid insertion slots for target
placed: List[int] = []
used: Set[int] = set()
counts_U = defaultdict(int)

def backtrack_U(indeg: Dict[int,int]):
    if len(placed) == len(U):
        # Try inserting target at every position 0..len(U)
        valid_slots = 0
        for k in range(len(placed) + 1):
            full_order = placed[:k] + [target] + placed[k:]
            if is_valid_full_order(full_order):
                valid_slots += 1
        counts_U[valid_slots] += 1
        return

    for u in sorted(U):
        if u not in used and indeg[u] == 0:
            placed.append(u)
            used.add(u)
            changed = []
            for w in covers[u]:
                if w in indeg:
                    indeg[w] -= 1
                    changed.append(w)
            backtrack_U(indeg)
            for w in changed:
                indeg[w] += 1
            used.remove(u)
            placed.pop()

backtrack_U(dict(initial_indeg))

# Compute invariant total (sum counts_U[s] * s)
total_orderings = sum(count * s for s, count in counts_U.items())

# Print the distribution
print("\nNumber of Blocks  Block size\n")
for size in sorted(k for k in counts_U.keys() if k > 0):
    count = counts_U[size]
    print(f"{count:6d} : {size:11d}  ({count} X {size}) = {count*size}")
print("-" * 40)
print(f"{'':11}Total orderings   {total_orderings}\n")
