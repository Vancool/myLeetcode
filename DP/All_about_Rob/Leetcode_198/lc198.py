class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        nums[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            nums[i] = max(nums[i] + nums[i-2], nums[i-1])
        return nums[len(nums) - 1]

'''
test case
[2,1,1,2]
一开始确定边界的时候第二个不会特殊处理

个人觉得这个人的解析很好
https://leetcode-cn.com/problems/house-robber-ii/solution/213-da-jia-jie-she-iidong-tai-gui-hua-jie-gou-hua-/
'''