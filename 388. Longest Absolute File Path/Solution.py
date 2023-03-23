class Solution:
    def lengthLongestPath(self, input: str) -> int:
        res, d = 0, {}
        for file in input.splitlines():
            depth = file.count("\t")
            if "." not in file:
                d[depth] = len(file) - depth
            else:
                curr = len(file) + sum([d[v] for v in range(depth)])
                res= max(res,curr)
        return res