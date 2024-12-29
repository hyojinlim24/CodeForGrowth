class Solution:
    def sum_digits(self, number: int) -> int:
        """
        Calculates the sum of the squares of the digits of a given number.

        :param number: The input number
        :return: The sum of the squares of its digits
        """
        return sum(int(digit) ** 2 for digit in str(number))

    def isHappy(self, n: int) -> bool:
        """
        Determines if a number is a "happy number".

        A happy number is a number that will eventually reach 1 when replaced
        by the sum of the squares of its digits. If a number loops endlessly
        in a cycle that does not include 1, it is not a happy number.

        :param n: The input number
        :return: True if the number is happy, False otherwise
        """
        seen = set()  # To track numbers we've already seen to avoid infinite loops

        while n != 1:
            if n in seen:
                return False  # The number is in a cycle
            seen.add(n)
            n = self.sum_digits(n)  # Replace n with the sum of the squares of its digits

        return True  # If we reach 1, the number is happy