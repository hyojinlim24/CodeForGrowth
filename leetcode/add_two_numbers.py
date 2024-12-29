from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two numbers represented as linked lists and returns the sum as a linked list.

        :param l1: First linked list representing a number
        :param l2: Second linked list representing a number
        :return: Linked list representing the sum of the two numbers
        """
        # Convert the first linked list to a string representing the number
        t1_total = self.linked_list_to_string(l1)

        # Convert the second linked list to a string representing the number
        t2_total = self.linked_list_to_string(l2)

        # Reverse the strings, add them as integers, then reverse the result and convert to a list
        result_number = list(str(int(t1_total[::-1]) + int(t2_total[::-1]))[::-1])

        # Convert the result list back to a linked list
        return self.list_to_linked_list(result_number)

    def linked_list_to_string(self, node: ListNode) -> str:
        """
        Converts a linked list to a string representation of its number.

        :param node: The head of the linked list
        :return: String representation of the number
        """
        result = ""
        while node:
            result += str(node.val)
            node = node.next
        return result

    def list_to_linked_list(self, lst: list) -> ListNode:
        """
        Converts a list of digits into a linked list.

        :param lst: List of digits
        :return: Linked list representing the digits
        """
        current = dummy_node = ListNode(0)
        for e in lst:
            current.next = ListNode(int(e))
            current = current.next
        return dummy_node.next