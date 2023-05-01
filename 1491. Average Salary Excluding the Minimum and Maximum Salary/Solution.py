class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        total = sum(salary[1:-1]) / (len(salary) - 2)
        return(total)