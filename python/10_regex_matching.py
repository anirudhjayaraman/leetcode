# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 17:07:20 2021

@author: Anirudh
"""

# =============================================================================
# Example 1:
# 
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:
# 
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:
# 
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:
# 
# Input: s = "aab", p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
# Example 5:
# 
# Input: s = "mississippi", p = "mis*is*p*."
# Output: false
# =============================================================================

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        