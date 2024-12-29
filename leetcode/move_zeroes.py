class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Move all 0's in the list to the end while maintaining the relative order of the non-zero elements.
        """
        insert_pos = 0  # Pointer to track where to place the next non-zero element
        
        # Move non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                # Only increment insert_pos when a non-zero element is placed
                if i != insert_pos:
                    nums[i] = 0
                insert_pos += 1
        
        # No need to explicitly move zeros as they are already placed by default