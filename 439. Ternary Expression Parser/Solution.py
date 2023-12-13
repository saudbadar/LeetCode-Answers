class Solution:
    def parseTernary(self, expression: str) -> str:
        stack, idx = [], len(expression) - 1

        while(idx >= 0):
            char = expression[idx]
            if(char in "TF0123456789"):
                stack.append(char)
            
            elif(char == "?"):
                onTrue, onFalse = stack.pop(), stack.pop()
                stack.append(onTrue if expression[idx - 1] == "T" else onFalse)
                idx -= 1
            idx -= 1
        return(stack[0])