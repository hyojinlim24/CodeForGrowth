class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Finds the majority element in the list using Boyer-Moore Voting Algorithm.
        
        :param nums: List of integers
        :return: The majority element
        """
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate