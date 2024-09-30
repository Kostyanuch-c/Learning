class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return list(map(lambda x: True if x + extraCandies >= max(candies) else False, candies))


if __name__ == '__main__':
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3

    print(Solution().kidsWithCandies(candies, extraCandies))
# 11081
