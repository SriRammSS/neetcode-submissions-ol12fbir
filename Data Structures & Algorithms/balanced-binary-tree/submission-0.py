
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if root is None:
                return 0
            left=height(root.left)
            right=height(root.right)

            return 1+max(left,right)
        if not root:
            return True
    
        if root.left or root.right is not None:
            left_sub=height(root.left)
            right_sub=height(root.right)
        else:
            return True
        

        diff=left_sub-right_sub

        if abs(diff) > 1:
            return False
        else:
            return True
        
        height(root)

    
        