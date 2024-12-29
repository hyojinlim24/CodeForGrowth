class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        :param string: Input string
        :return: Length of the longest substring with unique characters
        """
        # Initialize a set to store unique characters
        seen = set()
        left = 0  # Sliding window left pointer
        longest = 0

        # Iterate through the string with a right pointer
        for right in range(len(string)):
            # If the character is already in the set, shrink the window from the left
            while string[right] in seen:
                seen.remove(string[left])
                left += 1

            # Add the current character to the set
            seen.add(string[right])

            # Update the longest length
            longest = max(longest, right - left + 1)

        return longest