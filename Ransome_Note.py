#Easy Problem
# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return 
# true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
# Each letter in the magazine string can only be used once in your ransom note.


#Use Collections.Counter

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        temp = collections.Counter(ransomNote)
        temp2 = collections.Counter(magazine)
        
        return not temp - temp2



        
            