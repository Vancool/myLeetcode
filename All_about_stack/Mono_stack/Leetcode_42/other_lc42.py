from collections import deque
'''
Leetcode 42 接雨水
很经典的题目
最好的解法个人认为是使用单调栈

解法一、维护一个单调递减的栈,栈中存的是下标
'''
class Solution(object):
    def trap(self, height):
        if len(height) <= 2:
            return 0
        stack = []
        res = 0
        for i in range(len(height)):
            if len(stack) == 0 and height[i] == 0:
                continue
            while len(stack) > 0 and height[i] >= height[stack[-1]]:
                bottomIndex = stack.pop()
                bottomHeight = height[bottomIndex]
                if len(stack) == 0:
                    break
                leftIndex = stack[-1]
                leftHeight = height[leftIndex]
                topHeight = min(leftHeight, height[i])
                res += (topHeight - bottomHeight) * (i - leftIndex-1)
            stack.append(i)
        return res

'''
方法二，算每一列接的雨水
怎么算： 每列接的雨水是左边右边的最小高度减去现在的高度 * 1
使用dp:可以维护两个左边右边的最小高度的数组，然后直接查一下就好
比如左边的dp[i]记录的就是包括自己所在的0-i的最小高度
'''
class Solution(object):
    def trap(self, height):
        if len(height) <= 2:
            return 0
        res = 0
        dpLeft = [0] * len(height)
        dpRight = [0] * len(height)
        dpLeft[0] = height[0]
        dpRight[-1] = height[-1]
        for i in range(1,len(height)):
            dpLeft[i] = max(dpLeft[i-1], height[i])
        for i in range(len(height)-2,-1,-1):
            dpRight[i] = max(dpRight[i+1], height[i])
        for i in range(len(height)):
            H = min(dpLeft[i], dpRight[i]) - height[i]
            res += H * 1
        return res

'''
如何用双指针来节约空间呢？
如果maxLeft <= maxRight的话，那么左边第i个一定会用左边的maxLeft，那么每次只用更新左边然后移动就好
反之，则用右边的指针
'''
class Solution(object):
    def trap(self, height):
        if len(height) <= 2:
            return 0
        '''边界条件'''
        maxLeft = height[0]
        maxRight = height[-1]
        left = 1
        right = len(height)-2
        res = 0
        while left <= right:
            if maxLeft <= maxRight:
                #用左指针
                maxLeft = max(maxLeft, height[left])
                res += maxLeft - height[left]
                left += 1
            else:
                maxRight = max(maxRight, height[right])
                res += maxRight - height[right]
                right -= 1
        return res



a = Solution()
h = [0,1,0,2,1,0,1,3,2,1,1,1]
print(a.trap(h))
print("Done")
