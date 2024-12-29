class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):  # Iterate over all 32 bits
            result = result << 1  # Shift the result left by 1 to make space for the next bit
            result |= n & 1  # Get the least significant bit of n and add it to result
            n >>= 1  # Shift n right by 1 to process the next bit
        return result