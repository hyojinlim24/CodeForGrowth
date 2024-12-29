from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, head_a: ListNode, head_b: ListNode
    ) -> Optional[ListNode]:
        """
        Finds the intersection node of two singly linked lists, if it exists.

        :param head_a: Head of the first linked list
        :param head_b: Head of the second linked list
        :return: The intersection node, or None if no intersection exists
        """
        if not head_a or not head_b:
            return None

        # Initialize two pointers
        pointer_a, pointer_b = head_a, head_b

        # Traverse both lists; when a pointer reaches the end of one list,
        # move it to the head of the other list. If the lists intersect,
        # the pointers will eventually meet at the intersection node.
        while pointer_a != pointer_b:
            pointer_a = pointer_a.next if pointer_a else head_b
            pointer_b = pointer_b.next if pointer_b else head_a

        # Either both pointers are None (no intersection) or they meet at the intersection node
        return pointer_a