class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        lenPushPop, posPush, posPop = len(pushed), 0, 0
        lst = []
        while(posPush < lenPushPop):
            if(not lst or lst[-1] != popped[posPop]):
                lst.append(pushed[posPush])
                posPush += 1
            else:
                lst.pop()
                posPop += 1
        return(True if lst[::-1] == popped[posPop:] else False)