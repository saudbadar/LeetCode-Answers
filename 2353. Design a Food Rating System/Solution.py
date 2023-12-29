from sortedcontainers import SortedSet
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodRatingMap, self.foodCuisineMap, self.cuisineFoodMap = {}, {}, defaultdict(list)
        for food, cuisine, rate in zip(foods, cuisines, ratings):
            self.foodRatingMap[food], self.foodCuisineMap[food] = -rate, cuisine
            heapq.heappush(self.cuisineFoodMap[cuisine], (-rate, food))
        
    def changeRating(self, food: str, newRating: int) -> None:
        self.foodRatingMap[food] = -newRating
        cuisine = self.foodCuisineMap[food]
        heapq.heappush(self.cuisineFoodMap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while(self.foodRatingMap[self.cuisineFoodMap[cuisine][0][1]] != self.cuisineFoodMap[cuisine][0][0]):
            heapq.heappop(self.cuisineFoodMap[cuisine])
        return(self.cuisineFoodMap[cuisine][0][1])
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)