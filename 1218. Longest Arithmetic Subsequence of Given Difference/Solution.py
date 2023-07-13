class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        myDict = {}
        for num in arr:
            val = num - difference
            if(val in myDict):
                myDict[num] = myDict[val] + 1
            else:
                myDict[num] = 1
            
        return(max(myDict.values()))