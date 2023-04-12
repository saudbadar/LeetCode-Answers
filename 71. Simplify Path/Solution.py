class Solution:
    def simplifyPath(self, path: str) -> str:
        ret = []
        for temp in path.split("/"):
            if(not temp or temp == "."):
                continue
            elif(temp ==".."):
                if ret:
                    ret.pop()
            else:
                ret.append(temp)
        finalRet = "/" + "/".join(ret)
        return(finalRet)