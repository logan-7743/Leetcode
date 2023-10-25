# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True

            # Check if the current node's value is within the valid range (left < node.val < right)
            if not (left < node.val < right):
                return False

            # Recursively check the left and right subtrees
            return (
                valid(node.left, left, node.val) and
                valid(node.right, node.val, right)
            )

        # Start the validation with the entire tree, allowing for any values (-inf to +inf)
        return valid(root, float("-inf"), float("inf"))
