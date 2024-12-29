class Solution:
    def longestPalindrome(self, string: str) -> str:
        """
        Finds the longest palindromic substring in the given string.

        :param string: The input string
        :return: The longest palindromic substring
        """
        if len(string) <= 1 or string == string[::-1]:
            return string  # If the string is already a palindrome or has a length of 1

        def expand_around_center(left: int, right: int) -> str:
            """
            Expands around the center indices to find the longest palindrome.
            
            :param left: Left index of the current center
            :param right: Right index of the current center
            :return: The longest palindromic substring found in this expansion
            """
            while left >= 0 and right < len(string) and string[left] == string[right]:
                left -= 1
                right += 1
            return string[left + 1:right]

        longest = ""

        for i in range(len(string)):
            # Check for odd-length palindromes (center is at `i`)
            odd_palindrome = expand_around_center(i, i)
            # Check for even-length palindromes (center is between `i` and `i + 1`)
            even_palindrome = expand_around_center(i, i + 1)
            
            # Update the longest palindrome if needed
            longest = max(longest, odd_palindrome, even_palindrome, key=len)

        return longest