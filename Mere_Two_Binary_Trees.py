# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        # Check if both input trees are empty, return None if they are.
        if not t1 and not t2:
            return None

        # Get the values of the nodes in t1 and t2, or use 0 if they are None.
        v1 = t1.val if t1 else 0
        v2 = t2.val if t2 else 0

        # Create a new node with the sum of values from t1 and t2.
        root = TreeNode(v1 + v2)

        # Recursively merge the left and right subtrees.
        root.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        root.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)

        # Return the merged binary tree.
        return root

    # This code defines a method for merging two binary trees.
