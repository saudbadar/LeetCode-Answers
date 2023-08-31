class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ret, leftY, seenN  = 0, customers.count('Y'), 0
        minPen = leftY
        for idx, letter in enumerate(customers):
            if(letter == "Y"):
                leftY -= 1
            else:
                seenN += 1
            if((seenN + leftY) < minPen):
                ret = idx + 1
                minPen = (seenN + leftY)
        return(ret)