"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        def merge(root):
            child = root.child
            while(child.next):
                child = child.next
            if(root.next):
                child.next, root.next.prev = root.next, child
            root.next, current.child.prev, root.child = root.child, root, None
            
        current = head
        while(current):
            if(current.child):
                merge(current)
            current = current.next
        return(head)