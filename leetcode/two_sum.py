from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, return the indices
        of the two numbers such that they add up to the target.
        
        :param nums: List of integers.
        :param target: Target sum to find.
        :return: List containing two indices of the numbers that add up to target.
        """
        # Dictionary to store numbers and their indices
        store = {}

        # Iterate over the list of numbers
        for index, number in enumerate(nums):
            complement = target - number  # The value we're looking for

            # Check if the complement already exists in the dictionary
            if complement in store:
                # Return the indices of the current number and its complement
                return [store[complement], index]
            
            # Store the current number's index in the dictionary
            store[number] = index

        # If no solution is found (though it's assumed that there is always one solution)
        return []