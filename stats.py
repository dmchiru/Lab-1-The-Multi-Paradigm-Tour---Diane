"""
Lab 1: The Multi-Paradigm Tour -- Python implementation.

Run: python stats.py 4 8 15 16 23 42
Complete compute_stats() below. See the assignment,
Part B, for the full shared contract (all three language versions
must match it exactly).
"""

import sys
from typing import List, Tuple


def compute_stats(nums: List[int]) -> Tuple[float, float, int]:
    """
    Return (mean, median, mode).
    - median: for an even count, average the two middle values after sorting.
    - mode: the most frequent value; on a tie, the SMALLEST tied value.
    """

    mean = sum(nums) / len(nums)

    sorted_nums = sorted(nums)
    n = len(sorted_nums)

    if n % 2 == 1:
        median = float(sorted_nums[n // 2])
    else:
        median = (
            sorted_nums[n // 2 - 1] + sorted_nums[n // 2]
        ) / 2.0

    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    max_count = max(counts.values())

    mode = min(
        num
        for num, count in counts.items()
        if count == max_count
    )

    return mean, median, mode


def main() -> int:
    if len(sys.argv) < 2:
        return 1
    nums = [int(a) for a in sys.argv[1:]]
    mean, median, mode = compute_stats(nums)
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Mode: {mode}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
