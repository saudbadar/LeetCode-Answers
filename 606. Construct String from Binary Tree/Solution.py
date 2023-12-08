# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
      ret = ""

      def recursion(node):
        nonlocal ret
        ret += str(node.val)
        if(node.left or node.right):
          ret += "("
          if(node.left):
            recursion(node.left)
          ret += ")"
          if(node.right):
            ret += "("
            recursion(node.right)
            ret += ")"
      
      if(root):
        recursion(root)
      return(ret)
        