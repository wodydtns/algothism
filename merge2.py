import enum
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    for i, nums1_item in enumerate(nums1):
        if nums1_item > nums2[0]:
            nums1[i] = nums2[0]
            nums2[0] = nums1_item
            for key, value in enumerate(nums2[1:], start=1):
                if nums1_item <= value:
                    nums2[key-1] = nums1_item
                    break
                nums2[key-1] = nums2[key]


nums1 = [2, 8, 10]
m = 3
nums2 = [5]
n = 1
merge(nums1, m, nums2, n)
