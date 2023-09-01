class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lst, myDict, ret = [], {}, []
        for idx, num in enumerate(nums):
            num = -num
            myDict[num] = myDict.get(num, 0) + 1
            heapq.heappush(lst, num)
            if(idx >= k):
                myDict[-nums[idx - k]] -= 1
                if(myDict[-nums[idx - k]] == 0):
                    myDict.pop(-nums[idx - k])
            if(len(lst) >= k):
                while(lst[0] not in myDict):
                    heapq.heappop(lst)
                ret.append(-lst[0])
        return(ret)