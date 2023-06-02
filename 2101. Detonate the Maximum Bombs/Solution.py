class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        visited, queue, ret = set(), deque(), 0

        for idx, bomb in enumerate(bombs):
            if(idx in visited):
                continue
            queue.append(idx)
            depth, seen = 0, set()
            while(queue):
                loc, depth = queue.popleft(), depth + 1
                visited.add(loc)
                for newIdx, bomb in enumerate(bombs):
                    if(newIdx in seen or newIdx == idx):
                        continue
                    if(math.dist(bombs[loc][:2], bombs[newIdx][:2]) <= bombs[loc][2]):
                        queue.append(newIdx)
                        seen.add(newIdx)
            ret = max(ret, depth)
        return(ret)