from collections import deque

'''
Solution 是最优解法， O(n)
这题和daily temperature 有点像，就是如果情况根据上一个数值大小变化来记录index
同样的是使用栈来存储index求解
'''
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if heights == None or len(heights) == 0:
            return 0

        h = [0] + heights + [0]
        n = len(h)
        res = 0
        stack = deque()
        for i in range(n):
            while len(stack) > 0 and h[stack[-1]] > h[i]:
                right = i
                curH = h[stack.pop()]
                while h[stack[-1]] == curH:
                    stack.pop()
                left = stack[-1] + 1
                res = max(res, (right-left) * curH)
            stack.append(i)

        return res



class Solution2(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if heights == None or len(heights) == 0:
            return 0
        n = len(heights)
        leftIndex = [0] * n
        rightIndex = [0] * n
        leftIndex[0] = -1
        rightIndex[-1] = n
        for i in range(1,n): #get left smaller index
            temp = i-1
            while temp >=0 and heights[i] <= heights[temp]:
                temp = leftIndex[temp]
            leftIndex[i] = temp
        for i in range(n-1,-1,-1): #注意此处是从后往前动规的
            temp = i+1
            while temp<n and heights[i] <= heights[temp]:
                temp = rightIndex[temp]
            rightIndex[i] = temp
        res = 0
        for i in range(n):
            res = max(res, (rightIndex[i]-leftIndex[i]-1)*heights[i])
        return res

a = Solution2()
print(a.largestRectangleArea([2,1,2]))