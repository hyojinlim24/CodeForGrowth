class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Edge case: empty list or single element list
        if head is None or head.next is None:
            return True
        
        # Step 1: Find the middle of the linked list using the slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # Step 3: Compare the first half and the reversed second half
        left, right = head, prev
        while right:  # Only need to compare until the end of the reversed half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True