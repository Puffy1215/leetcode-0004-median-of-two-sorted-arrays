"""API for solving problem Median of Two Sorted Arrays"""

import statistics

LEN_MAX = 1000
LEN_MIN = 0

NUM_MAX = 10**6
NUM_MIN = -NUM_MAX

def _check_preconditions(nums1: list[int], nums2: list[int]) -> bool:
    for nums in [nums1, nums2]:
        if not sorted(nums):
            return False
        
        if not LEN_MIN <= len(nums) <= LEN_MAX:
            return False
        
        for x in nums:
            if not NUM_MIN <= x <= NUM_MAX:
                return False
    
    if not LEN_MIN + 1 <= len(nums1) + len(nums2) <= 2*LEN_MAX:
        return False
    
    return True


def _base_case_median_of_two_sorted_arrays(nums1: list[int], nums2: list[int]) -> int:
    m = len(nums1)
    n = len(nums2)

    assert m <= n
    assert m <= 2

    if m == 0:
        return statistics.median(nums2)


def _recursive_median_of_two_sorted_arrays(nums1: list[int], nums2: list[int]) -> int:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m = len(nums1)
    if m <= 2:
        return _base_case_median_of_two_sorted_arrays(nums1, nums2)
    

def median_of_two_sorted_arrays(nums1: list[int], nums2: list[int]) -> int:
    """Solves problem Median of Two Sorted Arrays"""

    assert _check_preconditions(nums1, nums2)

    return _recursive_median_of_two_sorted_arrays(nums1, nums2)