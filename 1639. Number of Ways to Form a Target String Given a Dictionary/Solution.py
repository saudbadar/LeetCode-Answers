class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n, mod = len(target), 10**9 + 7
        res = [1] + [0] * n
        for i in range(len(words[0])):
            count = collections.Counter(w[i] for w in words)
            for j in range(n - 1, -1, -1):
                res[j + 1] += res[j] * count[target[j]]
        return res[n] % mod