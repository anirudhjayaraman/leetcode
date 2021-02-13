# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 13:54:48 2021

@author: Anirudh
"""

# =============================================================================
# Example 1:
# 
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
# 
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# Example 3:
# 
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
# Example 4:
# 
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
# Example 5:
# 
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
# =============================================================================

from typing import List

nums1 = [1, 3, 5]
nums2 = [2, 7, 6, 9]
nums3 = [5, 5, 6]

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        traverse_till = (m + n) // 2
        median_type = (m + n) % 2
        
        if m == 0:
            if median_type == 0:
                return(0.5 * (nums2[traverse_till] + nums2[traverse_till - 1]))
            else: return nums2[traverse_till]
        if n == 0:
            if median_type == 0:
                return(0.5 * (nums1[traverse_till] + nums1[traverse_till - 1]))
            else: return nums1[traverse_till]
            
        sorted_list = list()
        
        idx1, idx2 = 0, 0
        
        for i in range(traverse_till + 1):
            if nums1[idx1] < nums2[idx2]:
                sorted_list += [nums1[idx1]]
                idx1 += 1
                if (idx1 == m):
                    sorted_list += nums2[idx2:(traverse_till + 1 - m)]
                    break
                
            elif nums1[idx1] > nums2[idx2]:
                sorted_list += [nums2[idx2]]
                idx2 += 1
                if idx2 == n:
                    sorted_list += nums1[idx1:(traverse_till + 1 - n)]
                    break
            else:
                sorted_list += [nums1[idx1], nums2[idx2]]
                idx1 += 1
                idx2 += 1
                if (idx1 == m):
                    sorted_list += nums2[idx2:(traverse_till + 1 - m)]
                    break
                if idx2 == n:
                    sorted_list += nums1[idx1:(traverse_till + 1 - n)]
                    break
        
        if median_type == 0:
            return(0.5 * (sorted_list[traverse_till] + sorted_list[traverse_till - 1]))
        else: return sorted_list[traverse_till]      


            
nums1 = [1,3]
nums2 = [2]        
Solution().findMedianSortedArrays(nums1, nums2)
        
nums1 = [1,2]
nums2 = [3,4]        
Solution().findMedianSortedArrays(nums1, nums2)

nums1 = [0,0]
nums2 = [0,0]        
Solution().findMedianSortedArrays(nums1, nums2)

nums1 = [2]
nums2 = []        
Solution().findMedianSortedArrays(nums1, nums2)        