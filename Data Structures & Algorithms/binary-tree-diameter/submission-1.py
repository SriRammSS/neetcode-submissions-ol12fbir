class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        fina=0
        if root is None:
            return -1
        left=self.diameterOfBinaryTree(root.left)
        right=self.diameterOfBinaryTree(root.right)

        return max(left,right)

        


        