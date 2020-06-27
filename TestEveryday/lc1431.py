class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        if not candies: return candies
        max_num = max(candies)
        res = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_num:
                res[i] = True
        return res