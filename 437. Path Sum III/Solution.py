# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ret, myDict = 0, defaultdict(int)
        def DFS(node, curSum):
            nonlocal ret
            if(not node):
                return()
            
            curSum += node.val
            if(curSum == targetSum):
                ret += 1
            ret += myDict[curSum - targetSum]
            myDict[curSum] += 1
            DFS(node.left, curSum)
            DFS(node.right, curSum)
            myDict[curSum] -= 1
        DFS(root, 0)
        return(ret)
            
        return(ret)