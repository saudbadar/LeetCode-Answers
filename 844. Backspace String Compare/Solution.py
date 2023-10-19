class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS, stackT = [], []
        for letter in s:
            if(letter != "#"):
                stackS.append(letter)
            elif(stackS):
                stackS.pop()
        for letter in t:
            if(letter != "#"):
                stackT.append(letter)
            elif(stackT):
                stackT.pop()
        return(stackS == stackT)