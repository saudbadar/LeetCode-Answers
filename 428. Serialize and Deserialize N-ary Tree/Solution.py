"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        lst = []
        def serializeHelper(node, lst):
            if(not node):
                return("")
            lst.append(str(node.val))
            lst.append(str(len(node.children)))
            for newNode in node.children:
                serializeHelper(newNode, lst)

        serializeHelper(root, lst)
        ret = ",".join(lst)
        return(ret)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if(not data):
            return(None)
        def deserializeHelper(queue):
            if(not queue):
                return(None)
            value, children = queue.popleft(), queue.popleft()
            root = Node(value, [])
            for _ in range(children):
                root.children.append(deserializeHelper(queue))
            return(root)
        lst, que = data.split(","), deque()
        [que.append(int(lst[i])) for i in range(len(lst))]            
        return(deserializeHelper(que))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))