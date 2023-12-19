class Solution:
    def frequencySort(self, s: str) -> str:
        myDict, ret = Counter(s), ""
        for key, amount in myDict.most_common():
            ret += key * amount
        return(ret)