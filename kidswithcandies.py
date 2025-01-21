
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        result = []
        for candy in candies:
            result.append(candy + extraCandies >= max_candies)
        return result
solution = Solution()
candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(solution.kidsWithCandies(candies, extraCandies))
