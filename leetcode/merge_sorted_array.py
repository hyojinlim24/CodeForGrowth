class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Merges two sorted arrays nums1 and nums2 in-place.
        After merging, nums1 will contain the merged sorted array.
        """
        # Pointers for nums1, nums2, and the current position to fill in nums1
        i, j, k = m - 1, n - 1, m + n - 1

        # Merge in reverse order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If any elements remain in nums2, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1