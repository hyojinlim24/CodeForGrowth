class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack = []
        # Mapping of closing brackets to opening brackets
        bracket_map = {")": "(", "]": "[", "}": "{"}

        # Iterate through each character in the string
        for char in s:
            if char in bracket_map:  # If it's a closing bracket
                # Pop the top element of the stack if it's not empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all brackets were properly closed; otherwise, they're unbalanced
        return not stack