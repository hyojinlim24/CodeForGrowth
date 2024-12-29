class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculates the number of distinct ways to climb a staircase with `n` steps,
        where you can climb 1 or 2 steps at a time.

        :param n: Total number of steps
        :return: Number of distinct ways to climb the staircase
        """
        # Base cases for when n is less than or equal to 3
        if n <= 3:
            return n

        # Initialize variables to represent the two previous steps in the sequence
        prev1, prev2 = 1, 2

        # Use a loop to calculate the nth Fibonacci number
        for _ in range(3, n + 1):
            current = prev1 + prev2  # Current step is the sum of the previous two steps
            prev1, prev2 = prev2, current  # Update for the next iteration

        return prev2