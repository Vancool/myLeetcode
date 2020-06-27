class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 1
        for i, val in enumerate(nums):
            while nums[i] != i+1:
                if nums[i] > len(nums):
                    nums[i] *= -1
                    break
                #elif  nums[i] < i+1:
                elif nums[i] <= 0:
                    # elif nums[i] <= 0 or nums[i] < i+1:
                    break
                else:
                    tmp = nums[nums[i]-1]
                    if tmp == nums[i]: break
                    nums[nums[i]-1] = nums[i]
                    nums[i] = tmp
                #print(nums)

        i = 1
        while i <= len(nums):
            if nums[i-1] != i:
                break
            i += 1
        return i

'''
没考虑的 case： 没考虑重复值
[1, 1]
'''
a = Solution()
nums = [3,4,-1,1]
print(a.firstMissingPositive(nums))