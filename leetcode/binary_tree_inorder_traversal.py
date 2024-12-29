from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs an iterative in-order traversal of a binary tree.

        :param root: Root node of the binary tree
        :return: List of node values in in-order sequence
        """
        res = []  # List to store the result of in-order traversal
        stack = []  # Stack to help traverse the tree iteratively

        while True:
            # Traverse to the leftmost node, adding nodes to the stack
            while root:
                stack.append(root)
                root = root.left

            # If the stack is empty, we have finished traversing the tree
            if not stack:
                return res

            # Process the last node in the stack
            node = stack.pop()
            res.append(node.val)  # Add the node's value to the result list

            # Move to the right subtree and repeat the process
            root = node.right