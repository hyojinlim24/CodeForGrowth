class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths of the strings are different, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Create a list to count the frequency of each character
        count = [0] * 26  # Assuming lowercase English letters only
        
        # Iterate over both strings simultaneously
        for char_s, char_t in zip(s, t):
            count[ord(char_s) - ord('a')] += 1  # Increment for char in s
            count[ord(char_t) - ord('a')] -= 1  # Decrement for char in t
        
        # If all counts are zero, the strings are anagrams
        return all(c == 0 for c in count)