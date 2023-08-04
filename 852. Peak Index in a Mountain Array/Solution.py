class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 1, len(arr) - 1

        while(left <= right):
            middle = left + (right - left) // 2
            if(arr[middle] < arr[middle + 1]):
                left = middle + 1
            elif(arr[middle] < arr[middle - 1]):
                right = middle - 1
            else:
                return(middle)
        return(-1)