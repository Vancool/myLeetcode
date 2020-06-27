class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in map:
                return [i, map[val]]
            map[nums[i]] = i
        return []

'''
two sum 的改进版
two sum用的是字典来存数，通过空间O（n）得到时间复杂度O（n）
那么倘若 two sum 用的是排序数组，那么可以用双指针（指针对撞）来剪枝
这样的话空间复杂度为O（n） 而时间复杂度也为O（n）
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            val = nums[left] + nums[right]
            if val == target:
                return [left, right]
            elif val < target:
                left += 1
            else:
                right -= 1
        return []
