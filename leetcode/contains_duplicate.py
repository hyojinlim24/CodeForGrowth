class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Checks if a list contains any duplicates.

        :param nums: List of integers
        :return: True if any value appears at least twice, False otherwise
        """
        # Use a set to track numbers we have seen
        seen = set()

        # Iterate through the list
        for number in nums:
            # If the number is already in the set, we found a duplicate
            if number in seen:
                return True
            # Otherwise, add the number to the set
            seen.add(number)

        # If we reach here, there are no duplicates
        return False