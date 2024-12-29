class Solution:
    def fizzBuzz(self, number: int) -> list[str]:
        """
        Generates a list of strings representing the FizzBuzz sequence up to the given number.

        :param number: The upper limit of the sequence (inclusive)
        :return: A list of strings representing the FizzBuzz sequence
        """
        # Initialize the result list to store the FizzBuzz output
        result = []

        # Define a dictionary for FizzBuzz rules (key: divisor, value: output string)
        rules = {
            3: "Fizz",
            5: "Buzz",
        }

        # Iterate from 1 to the given number (inclusive)
        for n in range(1, number + 1):
            # Initialize an empty string to build the FizzBuzz result for the current number
            answer = ""

            # Apply each rule in the dictionary
            for divisor, word in rules.items():
                # If the number is divisible by the divisor, append the corresponding word
                if n % divisor == 0:
                    answer += word

            # If no rules matched, use the number itself as a string; otherwise, use the answer
            result.append(answer or str(n))

        return result