class Solution(object):
    def findMaxLength(self, nums):
        if len(nums) < 2: return 0
        res = 0
        presum = {}
        presum[0] = -1
        val = 0
        for i in range(len(nums)):
            if nums[i] == 1: val += 1
            else: val -= 1
            if val in presum:
                res = max(res, i - presum[val])
            else:
                presum[val] = i
        return res
