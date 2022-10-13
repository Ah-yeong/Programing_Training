class Solution:
    def dfs(self, root, low, high):
        if root == None:
            return 0
    
        if root.val >= low and root.val <= high:
            return root.val + self.dfs(root.left, low, high) + self.dfs(root.right, low, high)
            
        if root.val > low:
            return self.dfs(root.left, low, high)
        
        elif root.val < high:
            return self.dfs(root.right, low, high)

        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.dfs(root, low, high)