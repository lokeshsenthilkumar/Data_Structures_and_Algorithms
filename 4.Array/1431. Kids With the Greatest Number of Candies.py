class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        r=max(candies)-extraCandies
        for i in range(len(candies)):
            candies[i]=candies[i]>=r
        return candies