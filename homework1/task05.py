from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    overall_sum = 0
    current_sum = 0
    for num in nums:
        current_sum = sum(nums[num:k+num])
        if current_sum > overall_sum:
            overall_sum = current_sum
    return overall_sum
