class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right, ret = 0, len(people) - 1, 0
        while(left <= right):
            tempVal = people[left] + people[right]
            if(tempVal > limit):
                right -= 1
            else:
                left += 1
                right -= 1
            ret += 1
        return(ret)