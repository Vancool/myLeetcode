class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums)
        count_zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count_zero += 1
            else:
                break
        for j in range(i+1, len(nums)):
            if nums[j] <= nums[j-1]:
                return False
            val = nums[j] - nums[j-1]
            if val > 1:
                if val - 1 > count_zero:
                    return False
                else:
                    count_zero -= val - 1
        return True

a = Solution()
nums = [0,1,2,0,5]
print(a.isStraight(nums))
print("Done")

