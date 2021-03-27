# Input:
# "tree"

# Output:
# "eert"

# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        temp = Counter(s)
        ans = ""
        for i,j in temp.most_common():
            ans += i*j
        return ans


#Couter.most_common() returns  the counter sorted

