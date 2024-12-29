class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # If n is less than or equal to 0, it's not a power of 3
        if n <= 0:
            return False
        # The maximum power of 3 within the integer range is 1162261467 (3^19)
        return 1162261467 % n == 0