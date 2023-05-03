class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        setOne, setTwo = set(num for num in nums1), set()
        for num in set(nums2):
            if(num in setOne):
                setOne.remove(num)
            else:
                setTwo.add(num)
        return([setOne, setTwo])