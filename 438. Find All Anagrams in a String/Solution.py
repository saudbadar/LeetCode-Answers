class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if(len(s) < len(p)):
            return(None)
        lenS, lenP, pMap, sMap, ret = len(s), len(p), Counter(p), Counter(), []

        for idx in range(lenS):
            sMap[s[idx]] += 1

            if(idx >= lenP):
                if(sMap[s[idx - lenP]] == 1):
                    del sMap[s[idx - lenP]]
                else:
                    sMap[s[idx - lenP]] -= 1
            
            if(pMap == sMap):
                ret.append(idx - lenP + 1)
        return(ret)