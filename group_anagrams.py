import collections


def group_anagrams(strs):
    hashmap = collections.defaultdict(list)

    for s in strs:
        hashmap["".join(sorted(s))].append(s)
    return hashmap.values()
