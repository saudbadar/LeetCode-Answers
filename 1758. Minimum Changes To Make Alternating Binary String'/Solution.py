class Solution:
    def minOperations(self, s: str) -> int:
        def count(lastVal):
            count = 0
            for letter in s:
                if(letter == lastVal):
                    count += 1
                    lastVal = '0' if lastVal == '1' else '1'
                else:
                    lastVal = letter
            return(count)
        count1, count2 = count('0'), count('1')
        return(min(count1, count2))