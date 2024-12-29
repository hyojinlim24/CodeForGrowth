from typing import Optional


# ListNode definition
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Determines if a linked list has a cycle using Floyd's Cycle Detection algorithm.

        :param head: Head of the linked list
        :return: True if the list contains a cycle, False otherwise
        """
        # Initialize two pointers, slow and fast
        slow, fast = head, head

        # Traverse the linked list
        while fast and fast.next:
            slow = slow.next  # Move slow pointer one step
            fast = fast.next.next  # Move fast pointer two steps

            # If the two pointers meet, there is a cycle
            if slow == fast:
                return True

        # If we exit the loop, there is no cycle
        return False