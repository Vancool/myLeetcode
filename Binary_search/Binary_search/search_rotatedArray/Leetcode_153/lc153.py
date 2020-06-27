class Solution(object):
    def findMin(self, nums):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums)-1
        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]
            mid = left + ((right - left) >> 1)
            if nums[left] <= nums[mid]:
                #左边有序
                left = mid + 1
            else:
                #右边有序
                left += 1
                right = mid
'''
个人觉得这题不是很难
https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
'''
a = Solution()
nums = [3,4,5,1,2]
print(a.findMin(nums))
print("Done")
