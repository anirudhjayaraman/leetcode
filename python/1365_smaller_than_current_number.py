# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 13:19:18 2021

@author: Anirudh
"""

# =============================================================================
# Given the array nums, for each nums[i] find out how many numbers in the array 
# are smaller than it. That is, for each nums[i] you have to count the number 
# of valid j's such that j != i and nums[j] < nums[i].
# 
# Return the answer in an array.
# =============================================================================

from typing import List

nums = [8,1,2,2,3]

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        for i in range(len(nums)):
            list2 = nums[0:i] + nums[i+1:]
            res[i] = sum([nums[i] > list2[j] for j in range(len(list2))])
        return(res)
        
 class Solution2:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = list()
        nums_sorted = sorted(nums)
        for i in range(len(nums)):
            res += [nums_sorted.index(nums[i])]
        return(res)
            
            
        

print(Solution().smallerNumbersThanCurrent(nums))
print(Solution2().smallerNumbersThanCurrent(nums))