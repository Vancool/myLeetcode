class Solution(object):
    def singleNumber(self, nums):
        res = 0
        for key in nums:
            res ^= key
        return res