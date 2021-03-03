# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 18:41:19 2021

@author: Anirudh
"""

# =============================================================================
# Implement pow(x, n), which calculates x raised to the power n (i.e. xn).
# 
#  
# 
# Example 1:
# 
# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:
# 
# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:
# 
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
# Constraints:
#
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# -10^4 <= x^n <= 10^4
# =============================================================================

# =============================================================================
# def myPow(x: float, n: int) -> float:
#     if n > 0:
#         if n == 1: return(x) 
#         else: return(x * myPow(x, n-1))
#     elif n < 0:
#         k = -n
#         if k == 1: return(1/x) 
#         else: return((1/(x * myPow(x, k-1))))
#     else: return(1)
# 
# print(myPow(2,10))
# print(myPow(2,-10))
# =============================================================================

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return(1)
        else:
            if n < 0: x, n = 1 / x, -n
            almost_sqrt = self.myPow(x, n // 2)
            if n % 2: return(almost_sqrt * almost_sqrt * x) 
            else: return(almost_sqrt * almost_sqrt)

print(Solution().myPow(2.000, 10))
print(Solution().myPow(2, -10))
print(Solution().myPow(0, 0))
print(Solution().myPow(0.00001, 2147483647))

        
        