class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        myMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        ret = []

        def backtrack(combo, digitLeft):
            nonlocal ret
            if(not digitLeft):
                ret.append(combo)
            else:
                for letter in myMap[digitLeft[0]]:
                    backtrack(combo + letter, digitLeft[1:])
        if(digits):
            backtrack("", digits)
        return(ret)