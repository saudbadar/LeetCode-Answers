class Solution:
    def __init__(self, nums: List[int]):
        self.original = nums
        

    def reset(self) -> List[int]:
        return(self.original)

    def shuffle(self) -> List[int]:
        combo, insert = self.original, []
        while(combo):
            idx = random.randrange(len(combo))
            insert.append(combo[idx])
            combo = combo[:idx] + combo[idx + 1:]
        return(insert)