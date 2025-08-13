"""
LC #242 - Valid Anagram (Easy)
Tags: hash-table, string, sorting
Time: O(n), Space: O(1)

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = {}

        for i in s:
            if i in char_count:
                char_count[i] += 1
            else:
                char_count[i] = 1
        
        for i in t:
            if i in char_count:
                char_count[i] -= 1
                if char_count[i] == 0:
                    del char_count[i]
            else:
                return False

        return len(char_count) == 0


        

