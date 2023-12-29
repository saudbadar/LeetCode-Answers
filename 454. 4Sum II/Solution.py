class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        length, myDict, ret = len(nums1), defaultdict(int), 0
        
        for one in nums3:
            for two in nums4:
                myDict[one + two] = myDict.get(one + two, 0) + 1
        
        for one in nums1:
            for two in nums2:
                temp = one + two
                if(-temp in myDict):
                    ret += myDict[-temp]
        return(ret)