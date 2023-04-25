class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        length = len(s)
        DP = [0 for _ in range(length + 1)]
        DP[-1] = 1

        for i in range(length - 1, -1, -1):
            if(s[i] == '0'):
                continue
            total, j = 0, i
            while(j < length and int(s[i:j + 1]) <= k):
                total += DP[j + 1]
                j += 1
            DP[i] = total % ((10 ** 9) + 7)
        return(DP[0])