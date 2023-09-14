class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for src, des in tickets:
            graph[src].append(des)
        
        for src in graph:
            graph[src].sort(reverse = True)
        
        stack = ['JFK']
        res = []
        
        while stack:
            
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            else:
                res.append(stack.pop())
        
        return res[::-1]