class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myCount, ret = Counter(nums), []
        for key, val in sorted(myCount.items(), key=lambda item: item[1], reverse= True)[:k]:
            ret.append(key)
        return(ret)