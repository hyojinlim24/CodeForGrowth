class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Use reversed() and convert it to a list to modify s in-place
        s[:] = list(reversed(s))