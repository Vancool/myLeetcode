class Solution(object):
    def largestRectangleArea(self, heights):
        if len(heights) == 1: return heights[0]
        left = [-1] * len(heights)
        right = [len(heights)] * len(heights)
        for i in range(1,len(heights)):
            tmp = i - 1
            while tmp >= 0 and heights[i] <= heights[tmp]:
                tmp -= 1
            left[i] = tmp
        for i in range(len(heights)-2,-1,-1):
            tmp = i+1
            while tmp <= len(heights)-1 and heights[i] <= heights[tmp]:
                tmp += 1
            right[i] = tmp
        res = 0
        for i in range(len(heights)):
            area = (right[i] - left[i]-1) * heights[i]
            res = max(res, area)
        return res

'''
超时，还是关于看左右的问题，可以考虑单调栈
'''
from collections import deque
class Solution(object):
    def largestRectangleArea(self, heights):
        if len(heights) == 1: return heights[0]
        stack = deque()
        heights = [0] + heights + [0] #哨兵
        stack.append(0)
        res = 0
        for i in range(1,len(heights)):
            while heights[stack[-1]] > heights[i]:
                curPos = stack.pop()
                curh = heights[curPos]
                while heights[stack[-1]] == curh:
                    stack.pop()

                area = curh * (i-stack[-1]-1)
                #这边一定是栈尾，不然对[2,1,2]会出错
                res = max(area, res)
            stack.append(i)
        return res


'''
注意test case: [2,1,2]
'''

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            #print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res