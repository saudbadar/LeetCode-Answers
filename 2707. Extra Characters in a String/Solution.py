class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [-1 for _ in range(len(s))]

        def recursion(string):
            if(not string):
                return(0)
            search, skip, loc = sys.maxsize, 0, len(s) - len(string)
            if(dp[loc] != -1):
                return(dp[loc])
            for word in dictionary:
                if(len(word) <= len(string) and string[:len(word)] == word):
                    search = min(search, recursion(string[len(word):]))
            skip = 1 + recursion(string[1:])
            dp[loc] = min(search, skip)
            return(dp[loc])
        return(recursion(s))