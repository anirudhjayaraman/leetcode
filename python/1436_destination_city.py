# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 11:53:20 2021

@author: Anirudh
"""

# =============================================================================
# You are given the array paths, where paths[i] = [cityAi, cityBi] means 
# there exists a direct path going from cityAi to cityBi. 
# Return the destination city, that is, the city without any path outgoing to 
# another city.
# 
# It is guaranteed that the graph of paths forms a line without any loop, 
# therefore, there will be exactly one destination city.
# =============================================================================

from typing import List

paths1 = [["B","C"],["D","B"],["C","A"]]
paths2 = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        to_cities = {x for l in paths for x in l[1:]}
        from_cities = {x for l in paths for x in l[:1]}
        return(list(to_cities.difference(from_cities))[0])
        
Solution().destCity(paths1)
Solution().destCity(paths2)