from typing import List


def majorityElement(nums: List[int]) -> int:
    majority_count = int(len(nums)/2)

    hashmap = {}

    for num in nums:
        if hashmap.get(num) != None:
            hashmap[num] = hashmap[num] + 1
        else:
            hashmap[num] = 1
        if hashmap[num] > majority_count:
            return num
    return -1


def majorityElement2(nums: List[int]) -> int:
    return sorted(nums)[int(len(nums)/2)]
