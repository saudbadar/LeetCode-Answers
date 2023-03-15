class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue, gap = deque(), False
        queue.append(root)

        while(queue):
            tempQueue = deque()
            while(queue):
                node = queue.popleft()
                if(node.left):
                    if(gap):
                        return(False)
                    tempQueue.append(node.left)
                else:
                    gap = True
                if(node.right):
                    if(gap):
                        return(False)
                    tempQueue.append(node.right)
                else:
                    gap = True
            queue = tempQueue
        return(True)