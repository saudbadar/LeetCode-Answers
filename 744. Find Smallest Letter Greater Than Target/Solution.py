class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        prevFound, left, right = letters[0], 0, len(letters) - 1
        while(left <= right):
            middle = (left + right) // 2
            if(letters[middle] > target):
                prevFound = letters[middle]
                right = middle - 1
            else:
                left = middle + 1
        return(prevFound)