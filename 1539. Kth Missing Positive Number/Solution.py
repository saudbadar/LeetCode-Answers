class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        valNeeded = 1

        for num in arr:
            while(valNeeded != num):
                k -= 1
                if(not k):
                    return(valNeeded)
                valNeeded += 1
            valNeeded += 1
        return(valNeeded + k - 1)