class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # Remove the rightmost '1' bit
            n &= (n - 1)
            count += 1
        return count