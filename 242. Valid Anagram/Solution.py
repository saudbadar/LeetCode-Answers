class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lengthS, lengthT, hashMap = len(s), len(t), {}
        if(lengthS != lengthT):
            return(False)
        
        for i in range(lengthS):
            sChar, tChar = s[i], t[i]
            hashMap[sChar] = hashMap.get(sChar, 0) + 1
            hashMap[tChar] = hashMap.get(tChar, 0) - 1
        
        for temp in hashMap.values():
            if(temp != 0):
                return(False)
        return(True)