class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2  # Sum of all numbers from 0 to n
        actual_sum = sum(nums)  # Sum of the numbers in the list
        return expected_sum - actual_sum  # The missing number is the difference