from typing import List


def missing_number_by_sort(nums: List[int]) -> int:
    nums.sort()

    if nums[-1] != len(nums):
        return len(nums)
    if nums[0] != 0:
        return 0

    for i in range(1, len(nums)):
        expected = nums[i-1] + 1
        print(expected)
        if expected != nums[i]:
            return expected
    return -1


nums = [0, 1, 2, 4]
missing_number_by_sort(nums)
