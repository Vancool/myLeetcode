'''
暴力解法， 时间复杂度为O（n*n）
'''
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if heights == None or len(heights) == 0:
            return 0
        n = len(heights)
        maxArea = [0] * n

        def getMaxArea(start, end, maxArea, heights):
            if start > end or start < 0 or end >= n:
                return
            if start == end:
                maxArea[start] = heights[start]
                return
            i = start
            smallVal = float("inf")
            smallIndex = start
            while i <= end:
                if smallVal >= heights[i]:
                    smallVal = heights[i]
                    smallIndex = i
                i += 1
            maxArea[smallIndex] = smallVal * (end - start + 1)
            getMaxArea(start, smallIndex - 1, maxArea, heights)
            getMaxArea(smallIndex + 1, end, maxArea, heights)

        getMaxArea(0, n - 1, maxArea, heights)
        return max(maxArea)

a = Solution()
print(a.largestRectangleArea([100,1,5,6,5,3]))
print("Done")