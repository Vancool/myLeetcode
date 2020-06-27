from collections import defaultdict
'''
这题好难啊
我以为是用基数排序，然而并不是
只是普通排序，只是把普通排序换了一个思路
'''
class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 0:
            return ""
        if len(nums) == 1:
            return str(nums[0])
        nums = map(str, nums)
        maxLen = 0
        for key in nums:
            maxLen = max(maxLen, len(key))
        tank = defaultdict(list)
        for i in range(maxLen):
            for key in nums:
                if i<len(key):
                    tank[key[i]].append(key)



