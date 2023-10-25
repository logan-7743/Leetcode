# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Define a helper function that takes the left and right indices as arguments.
        def helper(l, r):
            # Base case: If the left index is greater than the right index, return None.
            if l > r:
                return None
            
            # Calculate the middle index.
            mid = (r + l) // 2
            
            # Create a new TreeNode with the value at the middle index.
            root = TreeNode(nums[mid])
            
            # Recursively build the left and right subtrees.
            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)
            
            # Return the root of the subtree.
            return root
        
        # Call the helper function with the indices 0 and len(nums) - 1 to build the BST.
        return helper(0, len(nums) - 1)
