class Solution:
    temp = -100001
    result = 100001

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root.left != None:
            self.minDiffInBST(root.left)
            
        self.result = min(root.val - self.temp, self.result)
        self.temp = root.val
        
        if root.right!= None:
            self.minDiffInBST(root.right)
            
        return self.result