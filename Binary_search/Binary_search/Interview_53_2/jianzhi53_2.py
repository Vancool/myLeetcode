class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        其实也可以不处理边界然后直接二分循环
        只是处理边界会快一点点
        '''
        if nums[-1] != len(nums):
            return len(nums)
        if nums[0] != 0:
            return 0

        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == mid:
                left = mid + 1
            elif nums[mid] == mid + 1:
                right = mid - 1
        return left
