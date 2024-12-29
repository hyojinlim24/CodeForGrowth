class Solution:
    @staticmethod
    def longestCommonPrefix(strings: list[str]) -> str:
        """
        Finds the longest common prefix string among an array of strings.

        :param strings: List of strings
        :return: Longest common prefix as a string
        """
        if not strings:
            return ""  # Return an empty string if the input list is empty

        # Find the shortest string in the list (limits the possible prefix length)
        shortest_length = min(len(string) for string in strings)
        result = ""

        # Iterate through each character index up to the length of the shortest string
        for index in range(shortest_length):
            # Get the character at the current index from the first string
            current_char = strings[0][index]

            # Check if all strings have the same character at this index
            if all(string[index] == current_char for string in strings):
                result += current_char  # Add the character to the result
            else:
                break  # Stop if there is a mismatch

        return result