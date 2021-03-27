# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

#canonical method to reduce to simplest form then compare it.
#sorted method returns the new variable when used, sort uses the same var, we can say it's call by value.
def groupAnagrams(strs):
    groups = dict()
    for s in strs:
        key = ''.join(sorted(s))
        if key not in groups:
            groups[key] = [s]
        else:
            groups[key].append(s)
    return groups.values()

