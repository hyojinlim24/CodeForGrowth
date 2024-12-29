class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Finds the maximum area of water a container can hold given an array of heights.

        :param height: List of non-negative integers representing the heights of the container's walls
        :return: The maximum area of water that can be contained
        """
        # Initialize two pointers and a variable to store the maximum area
        left, right = 0, len(height) - 1
        max_area = 0

        # Use a two-pointer approach to find the maximum area
        while left < right:
            # Calculate the area between the two pointers
            width = right - left
            current_area = width * min(height[left], height[right])

            # Update the maximum area if the current area is larger
            max_area = max(max_area, current_area)

            # Move the pointer that points to the shorter height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area