class Solution(object):
    def subarraySum(self, nums, k):
        if len(nums) == 0: return 0
        res = 0
        for i in range(len(nums)):
            val = 0
            for j in range(i, len(nums)):
                val += nums[j]
                if val == k: res += 1
        return res

'''
https://leetcode-cn.com/problems/subarray-sum-equals-k/
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
如果数组都是正数或者是求最小的子数组可以直接用滑窗， 否则直接遍历只能用暴力解法 O(n^2)

改用前缀和求解
'''
from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        if len(nums) == 0: return 0
        hashmap = defaultdict(list)
        hashmap[0].append(-1)
        res = 0
        val = 0
        for i in range(len(nums)):
            val += nums[i]
            if val - k in hashmap:
                res += len(hashmap[val-k])
            hashmap[val].append(i)
        return res

'''
这边注意可以在哈希表中存个数而不是 index的数组，这样可以优化空间
'''
a = Solution()
nums = [0,0,0,0]
print(a.subarraySum(nums, 0))
