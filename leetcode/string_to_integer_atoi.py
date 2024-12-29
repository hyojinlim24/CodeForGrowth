from string import digits


class Solution:
    def myAtoi(self, string: str) -> int:
        # Strip leading and trailing whitespaces
        string = string.strip()

        # Edge case: if string is empty, return 0
        if not string:
            return 0
        
        # Handle the sign part
        sign = 1
        if string[0] == '-':
            sign = -1
            string = string[1:]
        elif string[0] == '+':
            string = string[1:]

        # Convert the number string
        result = 0
        for char in string:
            if char not in digits:
                break
            result = result * 10 + int(char)
        
        # Apply the sign and handle overflow
        result *= sign

        # Handle 32-bit integer overflow
        int_min, int_max = -2**31, 2**31 - 1
        if result < int_min:
            return int_min
        if result > int_max:
            return int_max

        return result