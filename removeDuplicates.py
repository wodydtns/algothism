from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if len(nums) <= 0:
        return 0
    curr = nums[0]
    cnt = 1
    for i in range(1, len(nums)):
        if curr != nums[i]:
            curr = nums[i]
            nums[cnt] = curr
