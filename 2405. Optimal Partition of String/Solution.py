class Solution:
    def partitionString(self, s: str) -> int:
        mySet, ret = set(), 0
        for letter in s:
            if(letter in mySet):
                mySet.clear()
                ret += 1
            mySet.add(letter)
        return(ret + 1)