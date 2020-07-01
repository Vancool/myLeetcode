class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        res = len(nums) + 1
        left, right = 0, 0
        val = 0
        while right < len(nums):
            val += nums[right]
            while val >= s and right >= left:
                res = min(res, (right - left + 1))
                val -= nums[left]
                left += 1
            right += 1
        return res if res <= len(nums) else 0


a = Solution()
nums = [2, 3, 1, 2, 4, 3]
print(a.minSubArrayLen(7, nums))
