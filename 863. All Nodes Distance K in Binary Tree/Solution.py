# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        myDict, queue, ret, visited = {}, deque(), [], set()

        def DFS(node):
            nonlocal myDict
            if(node.left):
                myDict[node.left] = node
                DFS(node.left)
            if(node.right):
                myDict[node.right] = node
                DFS(node.right)
        if(root):
            DFS(root)
        
        queue.append((target, 0))
        visited.add(target.val)

        while(queue):
            node, depth = queue.popleft()
            if(depth == k):
                ret.append(node.val)
            else:
                if(node in myDict and myDict[node].val not in visited):
                    visited.add(myDict[node].val)
                    queue.append((myDict[node], depth + 1))
                if(node.left and node.left.val not in visited):
                    visited.add(node.left.val)
                    queue.append((node.left, depth + 1))
                if(node.right and node.right.val not in visited):
                    visited.add(node.right.val)
                    queue.append((node.right, depth + 1))
        return(ret)