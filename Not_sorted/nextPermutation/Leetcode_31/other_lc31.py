class Solution(object):
    def nextPermutation(self, nums):
        if len(nums) == 1: return nums

        def reverseHelper(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        i = len(nums) - 2
        j = k = len(nums) - 1
        while i >= 0 and nums[j] <= nums[i]:
            i -= 1
            j -= 1
        if j != 0:
            while k > i and nums[k] <= nums[i]:
                k -= 1
            nums[k], nums[i] = nums[i], nums[k]
        reverseHelper(j, len(nums)-1)
'''
reverse 函数写得不熟
test case:
[1,1]
'''
a = Solution()
nums = [1,1]
a.nextPermutation(nums)
print(nums)





