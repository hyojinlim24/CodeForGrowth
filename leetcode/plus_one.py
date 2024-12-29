class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Start from the last digit
        for i in range(len(digits) - 1, -1, -1):
            # If the digit is less than 9, just increment it and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, set it to 0 and continue to the next digit
            digits[i] = 0
        
        # If we reach here, it means all digits were 9 and we need to add a leading 1
        return [1] + digits