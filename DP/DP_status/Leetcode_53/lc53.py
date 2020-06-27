class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return nums[0]
        dp = [[0]*len(nums) for _ in range(2)]
        dp[1][0] = nums[0]
        for i in range(1, len(nums)):
            dp[1][i] = max(nums[i], dp[i-1] + nums[i])
            dp[0][i] = max(dp[i-1], dp[1][i-1])
        return max(dp[1][len(nums) - 1], dp[0][len(nums)-1])
'''
https://leetcode-cn.com/problems/maximum-subarray/
解法一. dp 时间复杂度 O(n)
我自己写的dp的想法： 数组0表示第i个有没有包含， 数组1表示第i个有包含， 值表示到第i个时最大值
别人写的dp的想法： 数组表示到以包含i为结尾的所有字串的最大值，然后有个外部的变量res一直判断是否因为第i个值改变
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        dp = [0] * len(nums)
        dp[0] = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            res = max(res, dp[i])
        return res
'''
但是吧，其实我们的 i 只和 i-1 有关，因此空间复杂度可以不是O(n)
只要用一个变量存着i-1就好
这样看起来就很像 贪心法则 ，因为贪心的决策是只要第i-1个字串是能够让第i个字串增加值的，我们就算上
也就是说， dp[i-1] > 0 的话，就加上， 否则第 i 个自己净身出户作为头头开始，否则加起来也只会更小
题外话： 贪心是可线性时间解决的决策之一
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        cur = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            cur  = nums[i] if cur < 0 else cur + nums[i]
            res = max(res, cur)
        return res

'''
解法二、分治法 O(nlog(n))
 不知道为什么leetcode会要求用分治法
 我觉得明显用dp更快2333
 这个类似于归并排序，递归的解法
'''

class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return -1

        def count_crossMax(left, right, mid, nums):
            '''计算包含 mid, mid+1 的中间区间的最大值'''
            leftVal = nums[mid]
            curVal = leftVal
            for i in range(mid-1, left-1, -1):
                curVal += nums[i]
                leftVal = max(leftVal, curVal)
            rightVal = nums[mid+1]
            curVal = rightVal
            for i in range(mid+2, right+1):
                curVal += nums[i]
                rightVal = max(rightVal, curVal)
            return leftVal + rightVal

        def subMax(left, right, nums):
            if left == right:
                return nums[left]
            mid = left + (right - left) // 2
            left_max = subMax(left, mid, nums)
            right_max = subMax(mid+1, right, nums)
            cross_max = count_crossMax(left, right, mid, nums)
            return max(left_max, right_max, cross_max)
        return subMax(0, len(nums)-1, nums)







