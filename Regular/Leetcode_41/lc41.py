class Solution(object):
    def firstMissingPositive(self, nums):
        if len(nums) == 0: return 1
        dic = set()
        for key in nums:
            if key > 0:
                dic.add(key)
        for i in range(1,len(nums)+1):
            if i not in dic:
                return i
        return len(nums)+1

'''
我自己写的不太符合官方的要求： 常数级别的额外空间


可以用自己输入的nums数组模拟hash表
'''
class Solution(object):
    def firstMissingPositive(self, nums):
        if len(nums) == 0: return 1
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                '''注意此处不可以写成  
               nums[i]，nums[nums[i]-1] = nums[nums[i]-1],nums[i] 
                这样会先给 nums[i] 赋值导致 nums[nums[i]-1]出错
                '''
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1

'''
另一种想法.用自己的数组的下标模拟是否有这个数字，因为下标都是0 到 n-1的
如何判断是否有这个数字呢？ 负数代表有， 正数代表没有，这样不改变原值
'''


a = Solution()
nums = [3,4,-1,1]
print(a.firstMissingPositive(nums))