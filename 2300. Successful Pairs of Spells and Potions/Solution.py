class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ret, length = [], len(potions)
        for spell in spells:
            check = success // spell
            if((success % spell) != 0):
                check += 1
            val = length - bisect.bisect_left(potions, check)
            ret.append(val)
        return(ret)