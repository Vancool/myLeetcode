class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == None or len(nums) == 0:
            return[[]]
        if len(nums) == 1:
            return [nums]
        m = len(nums)
        def getSubPermute(nums, pre,res):
            if len(nums) == 1:
                res.append(pre + [nums[0]])
                return
            else:
                m = len(nums)
                for i in range(m):
                    new_nums = nums[0:i] + nums[i+1: len(nums)]
                    getSubPermute(new_nums, pre+[nums[i]], res)
        res = []
        pre = []
        getSubPermute(nums, pre, res)
        return res

a = Solution()
print(a.permute([1]))
print("Done!")
