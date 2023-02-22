# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret, lst = [], []

        def DFS(node):
            nonlocal lst
            if(not node.left and not node.right):
                lst.append(node.val)
                return(True)
            else:
                if(node.left and DFS(node.left)):
                    node.left = None
                if(node.right and DFS(node.right)):
                    node.right = None
            return(False)

        while(not DFS(root)):
            ret.append(lst.copy())
            lst.clear()
        ret.append([root.val])
        return(ret)
