class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def slidingWindow(change, amount):
            left, ret = 0, 0
            for right, letter in enumerate(answerKey):
                if(letter == change):
                    amount -= 1
                while(amount < 0):
                    if(answerKey[left] == change):
                        amount += 1
                    left += 1
                ret = max(ret, (right - left + 1))
            return(ret)
        return(max(slidingWindow('T', k), slidingWindow('F', k)))