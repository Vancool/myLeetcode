class Solution(object):
    def maxProduct(self, nums):
        if len(nums) == 1: return nums[0]
        dp = [[0] * len(nums) for _ in range(2)]
        dp[0][0] = nums[0] #当前最大值
        dp[1][0] = nums[0]#当前最小值
        for i in range(1, len(nums)):
            if nums[i] > 0:
                dp[0][i] = max(dp[0][i-1] * nums[i], nums[i])
                dp[1][i] = min(dp[1][i-1] * nums[i], nums[i])
            elif nums[i] < 0:
                dp[0][i] = max(dp[1][i-1] * nums[i], nums[i])
                dp[1][i] = min(dp[0][i-1] * nums[i], nums[i])
            else:
                dp[0][i] = 0
                dp[1][i] = 0
        return max(dp[0][:])

'''
解法一. DP 根据后面的正负区分两种状态
优化空间的dp
'''
class Solution1(object):
    def maxProduct(self, nums):
        if len(nums) == 1: return nums[0]
        preMax = nums[0]
        preMin = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                preMax = max(preMax * nums[i], nums[i])
                preMin = min(preMin * nums[i], nums[i])
            elif nums[i] < 0:
                tmp = preMax # 这边要注意加个 tmp 存着 preMax别让它改掉了
                preMax = max(preMin * nums[i], nums[i])
                preMin = min(tmp * nums[i], nums[i])
            else:
                preMax = preMin = 0
            res = max(preMax, res)
        return res


'''
解法二. 
左右各遍历一次， 如果是奇数个负数的话中途会得到最大值 
                如果是偶数个负数的话在结尾或者0之前会得到最大值
                碰到0的时候下一个重置成 nums[i]
'''
class Solution2(object):
    def maxProduct(self, nums):
        if len(nums) == 1: return nums[0]
        res = nums[0]
        pre = nums[0]
        for i in range(1, len(nums)):
            if pre == 0:
                pre = nums[i]
            else:
                pre = nums[i] * pre
            res = max(pre, res)
        pre = nums[-1]
        res = max(res, pre)
        for i in range(len(nums)-2,-1,-1):
            if pre == 0:
                pre = nums[i]
            else:
                pre = nums[i] * pre
            res = max(pre, res)
        return res
a = Solution2()
nums =[3,-1,4]
print(a.maxProduct(nums))
'''
解法三. 利用 res[i:j] = res[0:j] / res[0:i] 
记录 最小的正数 res[0:i] 和最大的负数[0：i]
我觉得这个解法不好记。
参考：
https://leetcode-cn.com/problems/maximum-product-subarray/solution/duo-chong-si-lu-qiu-jie-by-powcai-3/
'''