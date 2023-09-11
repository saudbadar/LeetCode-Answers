class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group, ret = defaultdict(list), []
        for idx, num in enumerate(groupSizes):
            group[num].append(idx)
            if(len(group[num]) == num):
                ret.append(group[num])
                del group[num]
        return(ret)
