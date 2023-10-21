class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        needVisit, queue, mySet = set(range(n)), deque(), set(range(n))
        
        for i in range(n):
            if(leftChild[i] in mySet):
                mySet.remove(leftChild[i])
            if(rightChild[i] in mySet):
                mySet.remove(rightChild[i])

        if(len(mySet) != 1):
            return(False)
        val = mySet.pop()
        queue.append(val)
        needVisit.remove(val)

        while(queue):
            node = queue.popleft()
            leftVal, rightVal = leftChild[node], rightChild[node]
            if(leftVal != -1):
                if(leftVal not in needVisit):
                    return(False)
                needVisit.remove(leftVal)
                queue.append(leftVal)
            if(rightVal != -1):
                if(rightVal not in needVisit):
                    return(False)
                needVisit.remove(rightVal)
                queue.append(rightVal)
        return(True if not needVisit else False)
                
