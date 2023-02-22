class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ret = [0 for _ in range(length + 1)]
        for update in updates:
            start, end, increment = update
            ret[start] += increment
            ret[end + 1] -= increment

        for idx in range(1, length):
            ret[idx] += ret[idx - 1]
        return(ret[:-1])