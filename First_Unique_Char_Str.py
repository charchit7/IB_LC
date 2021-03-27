# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = -1
        for i in range(len(s)):
            replaced_with_empty = s.replace(s[i],'',1)
            if s[i] not in replaced_with_empty:
                ans = i
                break  
                
        return ans