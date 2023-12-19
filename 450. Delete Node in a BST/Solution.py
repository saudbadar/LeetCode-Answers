# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

                
        # base case
        if not root: return None
        
        # base case (almost) with key found
        if root.val == key:
            # 1.a leaf or single child
            if not root.right: return root.left
            
            # 1.b leaf or single child
            if not root.left: return root.right
            
            # 2: both child node exist
            if root.left and root.right:
                # 2.a.1: start with right node of deleted node
                temp = root.right
                
                # 2.a.2: find minimum node in left subtree
                # we are going to replace minimum in left subtree with value at root
                while temp.left: 
                    temp = temp.left
                
                # 2.b: replace value with minimum value in right subtree
                root.val = temp.val
                
                # 2.c: ** key step ** recurse on root.right but with key  = root.val (min val in right subtree)
                root.right = self.deleteNode(root.right, root.val)
        
        # recursion steps
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
            
        return root