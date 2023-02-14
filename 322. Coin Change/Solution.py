class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        seen, queue, coinsUsed = {0}, collections.deque(), 0
        queue.append(0)
        
        if(amount == 0):
            return(coinsUsed)

        while(queue):
            newQueue = collections.deque()
            while(queue):
                val = queue.popleft()
                for coin in coins:
                    newVal = val + coin
                    if(newVal == amount):
                        return(coinsUsed + 1)
                    if(newVal not in seen and newVal < amount):
                        seen.add(newVal)
                        newQueue.append(newVal)
            queue = newQueue
            coinsUsed += 1
        return(-1)