import sys
from typing import List

min_diff = sys.maxsize
total = 0


def subset_diff(index: int, nums: List[int], subsum: int):
    global total, min_diff
    if index == len(nums):
        min_diff = min(min_diff, abs(((total - subsum) - subsum)))
        return

    subset_diff(index+1, nums, subsum+nums[index])
    subset_diff(index+1, nums, subsum)


nums = [3, 2, 4, 7, 1]
total = sum(nums)
subset_diff(0, nums, 0)
print(min_diff)
