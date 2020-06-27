class Solution(object):
    def canJump(self, nums):
        if len(nums) == 1:
            return True
        if len(nums) == 0:
            return False
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > 0:
                step = nums[i]
                if step + i >= len(nums):
                    dp[i] = True
                else:
                    j = 1
                    while j <= step:
                        idx = i + j
                        if dp[idx] == True:
                            dp[i] = True
                            break
                        else:
                            j += nums[idx]+1
        return dp[0]

a = Solution()
nums = [2,3,1,1,0]
print(a.canJump(nums))
print("Done")