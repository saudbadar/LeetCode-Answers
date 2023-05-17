class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return '0'

        stack = []
        for n in num:
            while stack and stack[-1] > n and k > 0:
                stack.pop()
                k -= 1
            stack.append(n)
        stack = stack[:-k] if k else stack
                
        return ''.join(stack).lstrip('0') or '0'