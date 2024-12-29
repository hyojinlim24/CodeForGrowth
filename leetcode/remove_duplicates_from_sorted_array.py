class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # Pointer to place the next unique element
        slow = 1

        # Iterate through the list starting from the second element
        for fast in range(1, len(nums)):
            # If the current element is different from the previous one, it's unique
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]  # Place the unique element at the 'slow' pointer
                slow += 1  # Move the slow pointer to the next position

        # After processing, 'slow' will be the length of the unique elements
        return slow