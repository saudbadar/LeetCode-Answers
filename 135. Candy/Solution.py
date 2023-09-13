class Solution:
    def candy(self, ratings: List[int]) -> int:
        length, ret = len(ratings), [1] * len(ratings)

        for idx in range(1, length):
            if(ratings[idx] > ratings[idx - 1]):
                ret[idx] = max(1 + ret[idx - 1], ret[idx])
        
        for idx in range(length - 2, -1, -1):
            if(ratings[idx + 1] < ratings[idx]):
                ret[idx] = max(1 + ret[idx + 1], ret[idx])
        return(sum(ret))