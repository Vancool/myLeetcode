from collections import deque
class Solution(object):
    def nextGreaterElements(self, nums):
        if not len(nums): return []
        if len(nums) == 1: return [-1]
        stack = deque()
        n = len(nums)
        res = []
        nums = nums + nums
        for i in range(len(nums)-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if i < n:
                if stack: res.append(stack[-1])
                else: res.append(-1)
            stack.append(nums[i])
        return res[::-1]
'''
不用把数组扩展两倍的写法
'''
from collections import deque
class Solution(object):
    def nextGreaterElements(self, nums):
        res = []
        stack = deque()
        n = len(nums)
        for i in range(2 * n - 1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            if i < n:
                if stack: res.append(stack[-1])
                else: res.append(-1)
            stack.append(nums[i % n])
        return res[::-1]
a = Solution()
nums = [1,2,1]
print(a.nextGreaterElements(nums))