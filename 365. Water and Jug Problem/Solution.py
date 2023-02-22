class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        queue, seen = collections.deque(), set()
        queue.append((0,0))
        seen.add((0,0))

        def add(valOne, valTwo):
            nonlocal queue, seen
            queue.append((valOne, valTwo))
            seen.add((valOne, valTwo))
        
        while(queue):
            jug1, jug2 = queue.popleft()
            if(jug1 == targetCapacity or jug2 == targetCapacity or (jug1 + jug2) == targetCapacity):
                return(True)
            if(jug1):
                if((0, jug2) not in seen):
                    add(0, jug2)
                if(jug2 != jug2Capacity):
                    diffTwo = jug2Capacity - jug2
                    swap = min(jug1, diffTwo)
                    newOne, newTwo = jug1 - swap, jug2 + swap
                    if((newOne, newTwo) not in seen):
                        add(newOne, newTwo)

            elif((jug1Capacity, jug2) not in seen):
                add(jug1Capacity, jug2)

            if(jug2):
                if((jug1, 0) not in seen):
                    add(jug1, 0)
                if(jug1 != jug1Capacity):
                    diffOne = jug1Capacity - jug1
                    swap = min(diffOne, jug2)
                    newOne, newTwo = jug1 + swap, jug2 - swap
                    if((newOne, newTwo) not in seen):
                        add(newOne, newTwo)
            elif((jug1, jug2Capacity) not in seen):
                add(jug1, jug2Capacity)
        return(False)