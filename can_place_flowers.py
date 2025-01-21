class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)

                if empty_left and empty_right:
                    flowerbed[i] = 1
                    count += 1

                    if count >= n:
                        return True

        return count >= n
flowerbed = [1, 0, 0, 0, 1]
n = 1
solution = Solution()
print(solution.canPlaceFlowers(flowerbed, n))
n = 2
print(solution.canPlaceFlowers(flowerbed, n))
