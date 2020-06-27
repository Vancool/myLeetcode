class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]

        left = 0
        right = len(nums)-1
        res = [-1,-1]
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        if left >= len(nums) or nums[left] != target:
            return res
        res[0] = left
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] > target:
                right = mid -1
            elif nums[mid] < target:
                left = mid + 1
            else:
                left = mid + 1
        res[1] = right
        return res



