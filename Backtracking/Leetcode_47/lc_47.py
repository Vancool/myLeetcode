class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        nums.sort()
        #used = [False] * len(nums)
        def Process(start):
            if start == len(nums)-1:
                res.append(list(nums))
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                nums[start], nums[i] = nums[i], nums[start]
                Process(start+1)
                nums[start], nums[i] = nums[i], nums[start]
        Process(0)
        return res
a =Solution()
nums = [0,1,0,0]
print(a.permuteUnique(nums))
print("Done")