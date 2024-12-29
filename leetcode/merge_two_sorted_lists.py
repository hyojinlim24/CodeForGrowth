class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        """
        Merges two sorted linked lists into a single sorted linked list.
        
        :param list1: First sorted linked list
        :param list2: Second sorted linked list
        :return: The merged sorted linked list
        """
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        # 'new_list' will be used to build the merged list
        new_list = dummy

        # Iterate over both lists until one of them is fully processed
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                # Append the smaller node from list1 to the merged list
                new_list.next = list1
                list1 = list1.next  # Move to the next node in list1
            else:
                # Append the smaller node from list2 to the merged list
                new_list.next = list2
                list2 = list2.next  # Move to the next node in list2

            # Move to the next node in the merged list
            new_list = new_list.next

        # If there are remaining nodes in either list, append them
        if list1 is not None:
            new_list.next = list1
        elif list2 is not None:
            new_list.next = list2

        # Return the merged list starting from dummy.next (since dummy is just a placeholder)
        return dummy.next