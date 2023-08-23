class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ret, remindar = "", columnNumber
        while(remindar > 0):
            value = (remindar - 1) % 26
            ret = chr(65 + value) + ret
            remindar = (remindar - 1) // 26
        return(ret)