"""API for solving problem Median of Two Sorted Arrays"""

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


def median_of_two_sorted_arrays(nums1: list[int], nums2: list[int]) -> int:
    """Solves problem Median of Two Sorted Arrays"""

    assert _check_preconditions(nums1, nums2)

    pass