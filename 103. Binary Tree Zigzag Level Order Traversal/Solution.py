class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack, ret, leftToRight = collections.deque(), [], True
        if(root):
            stack.append(root)
        
        while(stack):
            tempStack, lst = collections.deque(), []
            while(stack):
                temp = stack.popleft()
                lst.append(temp.val)
                if(temp.left):
                    tempStack.append(temp.left)
                if(temp.right):
                    tempStack.append(temp.right)
            if(leftToRight):
                ret.append(lst.copy())
            else:
                ret.append(lst[::-1].copy())
            stack, leftToRight = tempStack, not leftToRight
        return(ret)