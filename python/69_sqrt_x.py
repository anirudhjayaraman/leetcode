# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 20:03:15 2021

@author: Anirudh
"""

# =============================================================================
# Example 1:
# 
# Input: x = 4
# Output: 2
# Example 2:
# 
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
#  
# 
# Constraints:
# 
# 0 <= x <= 2^31 - 1
# =============================================================================

# =============================================================================
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x == 0 or x == 1: return(x)
#         else:
#             i = 1
#             while(x >= i * i):
#                 i += 1
#             return(i-1)
# =============================================================================

# =============================================================================
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x == 0 or x == 1: return(x)
#         else:
#             options = [2**(2*i) for i in range(1,17)]
#             options_roots = [2**i for i in range(1,17)]
#             for k in range(1, len(options)):
#                 if options[k] > x:
#                     i = options_roots[k-1]
#                     break
#             while(x >= i * i):
#                 i += 1
#             return(i - 1)
# =============================================================================
             
# =============================================================================
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x == 0 or x == 1: return(x)
#         else:
#             i = 1
#             tot = 1
#             while tot < x:
#                 tot += 2*i + 1    
#                 i += 1
#                 if tot == x: return(i)
#             return(i-1)
# =============================================================================
        
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return(x)
        elif x == 2:
            return (1)
        else:
            low, high = 0, x
            while low < high:
                mid = (low + high) // 2
                if mid * mid > x:
                    high = mid
                elif mid * mid < x:
                    low = mid + 1
                else:
                    return(mid)
            return(high - 1)

print(Solution().mySqrt(2**18))
[(i,Solution().mySqrt(i)) for i in range(20)]