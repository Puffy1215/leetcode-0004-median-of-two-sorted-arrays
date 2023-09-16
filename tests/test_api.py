"""Tests API for solving problem Median of Two Sorted Arrays"""

import random
import statistics
from typing import Callable

import pytest

from leetcode_0004_median_of_two_sorted_arrays import api


@pytest.mark.parametrize(
    ["result", "nums1", "nums2"],
    (
        [2, [1,3], [2]],
        [2.5, [1,2], [3,4]],
    )
)
def test_median_of_two_sorted_arrays(result: int, nums1: list[int], nums2: list[int]) -> None:
    """Tests solution for problem Median of Two Sorted Arrays"""

    assert api.median_of_two_sorted_arrays(nums1, nums2) == result


NumsRandResult = tuple[list[int], list[int]]
NumsRandType = Callable[[], NumsRandResult]


@pytest.fixture
def nums_rand() -> NumsRandType:
    """Fixture to generate random nums"""

    def _nums_rand() -> NumsRandResult:
        l = random.randint(api.LEN_MIN + 1, api.LEN_MAX)
        m = random.randint(api.LEN_MIN + 1, l)
        nums = [random.randint(api.NUM_MIN, api.NUM_MAX) for _ in range(l)]
        nums1 = sorted(nums[:m])
        nums2 = sorted(nums[m:])
        return nums1, nums2

    return _nums_rand

@pytest.mark.parametrize("run_count", range(10))
def test_median_of_two_sorted_arrays_rand(
    run_count: int,
    nums_rand: NumsRandType,  # pylint: disable=redefined-outer-name
) -> None:
    """Tests solution for problem Median of Two Sorted Arrays with random nums1 and nums2"""

    random.seed(run_count)

    nums1, nums2 = nums_rand()
    result = statistics.median(sorted(nums1 + nums2))

    test_median_of_two_sorted_arrays(result, nums1, nums2)