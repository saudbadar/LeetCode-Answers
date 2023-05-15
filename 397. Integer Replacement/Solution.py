class Solution:
    def integerReplacement(self, n: int) -> int:
        queue, mySet, ret = deque(), set(), 0
        queue.append(n)
        mySet.add(n)

        while(queue):
            tempQueue = deque()
            while(queue):
                val = queue.popleft()
                if(val == 1):
                    return(ret)
                if(val % 2):
                    if((val + 1) not in mySet):
                        mySet.add(val + 1)
                        tempQueue.append(val + 1)
                    if((val - 1) not in mySet):
                        if((val - 1) == 1):
                            return(ret + 1)
                        mySet.add(val - 1)
                        tempQueue.append(val - 1)
                else:
                    newVal = val // 2
                    if(newVal == 1):
                        return(ret + 1)
                    if(newVal not in mySet):
                        mySet.add(newVal)
                        tempQueue.append(newVal)
            queue = tempQueue
            ret += 1
        return(-1)