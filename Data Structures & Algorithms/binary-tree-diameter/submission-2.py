class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if root is None:
                return -1
            
            left=height(root.left)
            right=height(root.right)

            return 1+max(left,right)
       

        return 2+height(root.left)+height(root.right)
        

        


        


        