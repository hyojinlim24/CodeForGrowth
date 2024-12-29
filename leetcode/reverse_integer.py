class Solution:
    def reverse(self, number: int) -> int:
        reverse: int = 0
        negative: bool = number < 0

        # If number is negative, make it positive for ease of manipulation
        if negative:
            number *= -1

        # Reverse the digits using arithmetic
        while number > 0:
            last_digit = number % 10  # Get the last digit
            reverse = (reverse * 10) + last_digit  # Append it to reverse
            number = number // 10  # Remove the last digit from the number

        # Restore the sign if the number was negative
        if negative:
            reverse = reverse * -1

        # Check for 32-bit overflow (the valid range for 32-bit signed integers is -2^31 to 2^31 - 1)
        if reverse > 2**31 - 1 or reverse < -2**31:
            return 0  # Return 0 if overflow occurs

        return reverse