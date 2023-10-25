# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            # Base case: if the node is None, it's a balanced subtree with depth 0
            if root is None:
                return [True, 0]
            
            # Recursively calculate the balance and depth of the left and right subtrees
            left, right = dfs(root.left), dfs(root.right)
            
            # Check if the current subtree is balanced by considering left and right subtrees
            balance = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            
            # Calculate the depth of the current subtree
            return [balance, 1 + max(left[1], right[1])]
        
        # Call the DFS function on the root of the binary tree and return its balance result
        return dfs(root)[0]
