class Solution:
    @staticmethod
    def findTheDifference(s: str, t: str) -> str:
        """
        Finds the extra character in string t that is not present in string s.

        :param s: Original string
        :param t: String t with one additional character
        :return: The additional character in t
        """
        result = 0

        # XOR all characters in both strings
        for char in s + t:
            result ^= ord(char)

        # Convert the result back to a character
        return chr(result)