class Solution:
    def isValid(self, s: str) -> bool:
        stack, myMap = [], {']': '[', ')': '(', '}': '{'}
        for letter in s:
            if(letter in myMap):
                if(not stack or myMap[letter] != stack.pop()):
                    return(False)
            else:
                stack.append(letter)
        return(True if not stack else False)