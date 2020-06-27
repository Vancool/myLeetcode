from collections import deque
'''
可能会比较疑惑单调栈为什么能解决问题。
单调栈的典型用途是用于找到数组中下一个比自身大的元素（the next greater element, NGE）
原来是用堆来做，这样也可以获得最大值，但是复杂度为 n* log(k)
用双端队列维护一个单调栈，使得每次都能从头得到最大值 复杂度为 O(n)
注意双端队列里面存的是下标，不然没有办法判断是否要排除掉现在的最大值
（因为它已经出了窗口了
很有意思，我比较推荐这种做法比较好想一些

'''
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 1:
            return nums
        res = []
        window = deque()
        for i in range(len(nums)):
            while len(window) > 0 and window[0] <= i - k:
                window.popleft()
            while len(window) > 0 and nums[window[-1]] < nums[i]:
                window.pop()
            window.append(i)
            if i >= k-1:
                res.append(nums[window[0]])
        return res


'''
可以用dp来做
因为实际上是找到左边界和右边界的最大值
如果是找最大值或者最小值可以这么用
'''
class Solution1(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 1:
            return nums
        res = []
        leftdp = [0]*len(nums)
        leftdp[0] = nums[0]
        rightdp = [0] * len(nums)
        rightdp[-1] = nums[-1]
        for i in range(1,len(nums)):
            if i % k == 0:
                leftdp[i] = nums[i]
            else:
                leftdp[i] = max(leftdp[i-1], nums[i])
        for i in range(len(nums)-2, -1,-1):
            if i % k == 0:
                rightdp[i] = nums[i]
            else:
                rightdp[i] = max(rightdp[i+1], nums[i])
        for i in range(0, len(nums)-k+1):
            j = i + k - 1
            res.append(max(rightdp[i], leftdp[j]))
        return res
a = Solution1()
nums = [7,2,4]
print(a.maxSlidingWindow(nums, 2))

