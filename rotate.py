from typing import List


def rotate(nums: List[int], k: int) -> None:
    temp = [0] * len(nums)

    for i, elem in enumerate(nums):
        temp[(i+k) % len(nums)] = nums[i]
    nums[:] = temp
    print(nums)


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
