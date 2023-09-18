"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if(not root):
            return(None)
        dummy = prev = Node(-1)

        def inorder(node):
            nonlocal prev
            if(not node):
                return(None)
            inorder(node.left)
            prev.right, node.left, prev = node, prev, node
            inorder(node.right)
        inorder(root)
        dummy.right.left, prev.right = prev, dummy.right
        return(dummy.right)