class Solution:
    def titleToNumber(self, column_title: str) -> int:
        score = 0
        for char in column_title:
            score = score * 26 + (ord(char) - ord('A') + 1)
        return score