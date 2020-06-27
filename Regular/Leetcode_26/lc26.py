class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 1 or len(nums) == 0:
            return len(nums)
        index = 1
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                i += 1
            else:
                nums[index] = nums[i]
                i += 1
                index += 1
        nums = nums[0: index]
        print(nums)
        return index

a = Solution()
nums =[0 ,0,1,1,1,2,2,3,3,4]
print(a.removeDuplicates(nums))