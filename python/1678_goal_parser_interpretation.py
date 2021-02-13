# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 11:20:16 2021

@author: Anirudh
"""

class Solution:
    def interpret(self, command:str) -> str:
        """
        :type command: str
        :rtype: str
        """
        return(command.replace("()", "o").replace("(al)", "al"))
        
Solution().interpret("G()(al)")
        