class Solution(object):
    def findMin(self, nums):
        if nums == None or len(nums)==0:
            return -1
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while left <= right:
            while left <= right and nums[left] == nums[right]:
                left += 1
            if left >= right:
                return nums[right]
            if nums[left] < nums[right]:
                return nums[left]
            mid = left + (right - left) // 2
            while left <= mid and nums[left] == nums[mid]:
                left += 1
            if left > mid:
                continue
            if nums[left] < nums[mid]:
                left = mid + 1
            else:
                left = left + 1
                right = mid
'''
https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/
我觉得自己的解法更好呢，只是写得很冗杂，但是很容易看懂
但是思路都是一样的，都是二分查找
test case
1. [2,0,1]
'''
a = Solution()
nums = [2,0,1]
a.findMin(a.findMin(nums))
print("Done")
