class Solution:
    def __init__(self, nums: List[int]):
        self.myDict = defaultdict(list)
        for idx, num in enumerate(nums):
            self.myDict[num].append(idx)
        

    def pick(self, target: int) -> int:
        return(random.choice(self.myDict[target]))