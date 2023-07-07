class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        max_heap, min_heap = [], []
        for i in range(len(weights) - 1):
            v = weights[i] + weights[i + 1]
            heapq.heappush(min_heap, v)
            heapq.heappush(max_heap, -v)
            if len(min_heap) > k - 1:
                heapq.heappop(min_heap)
                heapq.heappop(max_heap)
        return sum(min_heap) + sum(max_heap)