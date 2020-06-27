class Solution(object):
    def productExceptSelf(self, nums):
        if len(nums) <= 1: return nums
        left = [1]
        pre = 1
        for i in range(len(nums)-1):
            pre *= nums[i]
            left.append(pre)
        pre = 1
        for i in range(len(nums)-1, -1,-1):
            left[i] *= pre
            pre *= nums[i]
        return left


'''
另一种只有一种循环的方法
双指针，不显式表示前缀积的数组
'''
class Solution(object):
    def productExceptSelf(self, nums):
        if len(nums) <= 1: return nums
        preleft = preright = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] *= preleft
            res[len(nums)-1-i] *= preright
            preleft *= nums[i]
            preright *= nums[len(nums)-1-i]
        return res

