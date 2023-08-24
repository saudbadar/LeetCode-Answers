class Solution:
    def reorganizeString(self, s: str) -> str:
        lst, counter, ret = [], Counter(s), ""
        for key, item in counter.items():
            heapq.heappush(lst, (-item, key))
        
        def helper(key, item):
            nonlocal lst, ret
            ret += key
            if(item != -1):
                heapq.heappush(lst, (item + 1, key))

        while(lst):
            valOne, keyOne = heapq.heappop(lst)
            if(not ret or ret[-1] != keyOne):
                helper(keyOne, valOne)  
            elif(lst):
                valTwo, keyTwo = heapq.heappop(lst)
                helper(keyTwo, valTwo)
                heapq.heappush(lst, (valOne, keyOne))
            else:
                break
        return(ret if len(ret) == len(s) else "")