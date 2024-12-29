class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter the string to keep only alphanumeric characters and convert to lowercase
        cleaned_string = "".join(filter(str.isalnum, s)).lower()

        # Check if the cleaned string is equal to its reverse
        return cleaned_string == cleaned_string[::-1]