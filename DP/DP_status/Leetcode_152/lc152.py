class Solution(object):
    def maxProduct(self, nums):
        if len(nums) == 1: return nums[0]
        left = [0] * (len(nums)+ 1)
        right = [0] * (len(nums)+1)
        left[0] = 1
        right[-1] = 1
        for i in range(len(nums)):
            if left[i] * nums[i] > 0:
                left[i+1] = left[i] * nums[i]
            else:
                left[i+1] = nums[i]
        for i in range(len(nums)-1,-1,-1):
            if right[i+1] * nums[i] > 0:
                right[i] = right[i+1] * nums[i]
            else:
                right[i] = nums[i]
        res = -float('inf')
        for i in range(len(left)):
            res = max(res, left[i] * right[i])
        return res

'''
这题我不会，原来是两个状态用dp
'''
a = Solution()
nums = [2,3,-2,-4,2]
print(a.maxProduct(nums))


