# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 16:29:02 2021

@author: Anirudh
"""

# =============================================================================
# Given a sorted (in ascending order) integer array nums of n elements and a 
# target value, write a function to search target in nums. If target exists, 
# then return its index, otherwise return -1.
# =============================================================================

from typing import List

nums1 = [-1,0,3,5,9,12]
target1 = 9

nums2 = [-1,0,3,5,9,12] 
target2 = 2

def binary_search(nums: List[int], target: int, left = 0, right = len(nums)-1) -> int:
    if left >= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return(mid)
        elif target > nums[mid]:
            return(binary_search(nums, target, mid + 1, len(nums) - 1)) 
        elif target < nums[mid]:
            return(binary_search(nums, target, 0, mid - 1))
    else:
        return(-1)


class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return(nums.index(target))
        except ValueError:
            return(-1)
            
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return(mid)
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return(-1)
        
        
        
            
print(Solution1().search(nums = nums1, target = target1))
print(Solution2().search(nums = nums2, target = target2))