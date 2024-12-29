from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Finds the intersection of two arrays, including duplicate elements based on their occurrences.

        :param nums1: First list of integers
        :param nums2: Second list of integers
        :return: A list containing the intersection of nums1 and nums2
        """
        # Count the frequency of each element in both lists
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

        # Result list to store the intersection elements
        result = []

        # Iterate through the elements and their counts in the first counter
        for key, value in counter1.items():
            if key in counter2:
                # Find the minimum occurrence of the current key in both counters
                min_count = min(value, counter2[key])
                # Add the key to the result list, repeated `min_count` times
                result.extend([key] * min_count)

        return result