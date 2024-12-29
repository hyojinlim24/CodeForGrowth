class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Finds the index of the first non-repeating character in a string.

        :param s: Input string
        :return: Index of the first unique character, or -1 if none exists
        """
        # Step 1: Count the frequency of each character using a dictionary
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Step 2: Find the first character with a count of 1
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i

        # If no unique character is found, return -1
        return -1