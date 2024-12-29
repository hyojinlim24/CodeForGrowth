class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Returns the index of the first occurrence of `needle` in `haystack`,
        or -1 if `needle` is not part of `haystack`.

        :param haystack: The string to search within
        :param needle: The substring to search for
        :return: Index of the first occurrence of `needle`, or -1 if not found
        """
        # Edge case: If needle is an empty string, return 0
        if not needle:
            return 0

        # Use the built-in `find` method to locate the substring
        return haystack.find(needle)