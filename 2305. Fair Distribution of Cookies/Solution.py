class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        lst, ret, avg = [0 for _ in range(k)], sys.maxsize, sum(cookies)/k
        if(k==8):
            return(max(cookies))

        def recursion(newLst):
            nonlocal ret, lst
            if(not newLst):
                ret = min(ret, max(lst))
            else:
                for i in range(k):
                    if(lst[i] < avg):
                        lst[i] += newLst[0]
                        recursion(newLst[1:])
                        lst[i] -= newLst[0]
        recursion(cookies)
        return(ret)