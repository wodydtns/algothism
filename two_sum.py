from typing import List


def tow_sum(nums: List[int], target: int) -> List[int]:
    hashtable_dict = {}
    for i in range(0, len(nums)):
        value = target - nums[i]
        if hashtable_dict.get(value) is not None and hashtable_dict[value] != i:
            return ([i, hashtable_dict[value]])
        hashtable_dict[nums[i]] = i
    return [-1, -1]
