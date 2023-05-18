class Solution:
    def canCross(self, stones: List[int]) -> bool:
        visited, stoneSet, lastStone, queue = set(), set(stones), stones[-1], deque()
        visited.add((0,0))
        queue.append((0,0))

        while(queue):
            curStone, prevJump = queue.popleft()
            if(curStone == lastStone):
                return(True)
            newPos = curStone + prevJump
            if(newPos in stoneSet and (newPos, prevJump) not in visited):
                visited.add((newPos, prevJump))
                queue.append((newPos, prevJump))
            newPos += 1
            if(newPos in stoneSet and (newPos, prevJump + 1) not in visited):
                visited.add((newPos, prevJump + 1))
                queue.append((newPos, prevJump + 1))
            newPos -= 2
            if(newPos in stoneSet and (newPos, prevJump - 1) not in visited):
                visited.add((newPos, prevJump - 1))
                queue.append((newPos, prevJump - 1))
        return(False) 