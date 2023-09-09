"""Tests API for solving problem Median of Two Sorted Arrays"""

import pytest

from leetcode_0004_median_of_two_sorted_arrays import api


@pytest.mark.parametrize(
    ["result", "nums1", "nums2"],
    (
        [..., ...],
        [..., ...],
    )
)
def test_median_of_two_sorted_arrays(result: int, nums1: list[int], nums2: list[int]) -> None:
    """Tests solution for problem Median of Two Sorted Arrays"""

    assert api.median_of_two_sorted_arrays(nums1, nums2) == result