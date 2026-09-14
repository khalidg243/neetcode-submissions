# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        elif not root:
            return False

        if root.val == subRoot.val and self.isSameTree(root,subRoot):
                return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def isSameTree(self,list1,list2):
        if not list1 and not list2:
            return True
        elif not list1 or not list2:
            return False
        elif list1.val != list2.val:
            return False
        
        return (self.isSameTree(list1.left , list2.left) and self.isSameTree(list1.right , list2.right))