class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helperFunction(newIn, newPost):
            if(not newIn):
                return(None)
            tempHeader = TreeNode(val = newPost[-1])
            insertIn = newIn.index(newPost[-1])
            if(insertIn != 0):
                tempHeader.left = helperFunction(newIn[:insertIn], newPost[:insertIn])
            tempHeader.right = helperFunction(newIn[insertIn + 1:], newPost[insertIn :-1])
            return(tempHeader)
        
        return(helperFunction(inorder, postorder))