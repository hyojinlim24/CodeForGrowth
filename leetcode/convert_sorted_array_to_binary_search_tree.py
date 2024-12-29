from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Converts a sorted array into a height-balanced binary search tree.

        :param nums: Sorted list of integers
        :return: Root node of the height-balanced BST
        """
        # Base case: If the array is empty, return None
        if not nums:
            return None

        # Find the middle element of the list
        middle = len(nums) // 2

        # Create the root node using the middle value
        root_node = TreeNode(nums[middle])

        # Recursively construct the left subtree using the left half of the array
        root_node.left = self.sortedArrayToBST(nums[:middle])

        # Recursively construct the right subtree using the right half of the array
        root_node.right = self.sortedArrayToBST(nums[middle + 1:])

        return root_node


def print_tree(node: Optional[TreeNode], level=0, prefix="Root: "):
    """
    Helper function to print the binary tree in a readable format.
    """
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.val))
        if node.left or node.right:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")