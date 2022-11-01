from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = int((low+high) / 2)
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    print(low)
    return low


nums = [1, 3, 5, 6]
target = 0
searchInsert(nums, target)
