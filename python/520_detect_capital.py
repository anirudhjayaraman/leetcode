class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if(len(word) == 1):
            return(True)
        return((word.upper() == word) or (word.lower() == word) or ((word[0].upper() == word[0]) and (word[1:].lower() == word[1:])))
    
print(Solution().detectCapitalUse('Hello'))  # True
print(Solution().detectCapitalUse('HEllo'))  # False
print(Solution().detectCapitalUse('HELLO'))  # True
print(Solution().detectCapitalUse('HellO'))  # False