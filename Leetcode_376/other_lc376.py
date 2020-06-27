class Solution(object):
    def wiggleMaxLength(self, nums):
        if len(nums) <= 1: return len(nums)
        dp = [[0]*2 for _ in range(len(nums))]
        dp[0][1] = 1
        dp[0][0] = 1
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i][0] = max(dp[i][0], dp[j][1]+1)
                 #   dp[i][1] = max(dp[i][1], dp[i-1][1])
                elif nums[i] < nums[j]:
                    dp[i][1] = max(dp[i][1], dp[j][0]+1)
                #    dp[i][0] = max(dp[i][0], dp[i-1][0])
                else:
                    dp[i] = dp[j]
        return max(dp[len(nums)-1])

class Solution(object):
    def wiggleMaxLength(self, nums):
        if len(nums) <= 1: return len(nums)
        dp = [[1]*2 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                dp[i][0] = max(dp[i][0], dp[i-1][1]+1)
                dp[i][1] = max(dp[i][1], dp[i-1][1])
            elif nums[i] < nums[i-1]:
                dp[i][1] = max(dp[i][1], dp[i-1][0]+1)
                dp[i][0] = max(dp[i][0], dp[i-1][0])
            else:
                dp[i] = dp[i-1]
        return max(dp[len(nums)-1])

class Solution(object):
    def wiggleMaxLength(self, nums):
        if len(nums) <= 1: return len(nums)
        pre = [1] * 2
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                pre[0] = max(pre[0], pre[1]+1)
            elif nums[i] < nums[i-1]:
                pre[1] = max(pre[1], pre[0]+1)
        return max(pre)


'''
单调栈做法
其实就是维护一个隐式的单调栈，只要记录一下维护的单调栈单调性变了几次就好啦
'''
class Solution(object):
    def wiggleMaxLength(self, nums):
        count = 1
        status = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                if status < 0 or status == 0:
                    count += 1
                    status = 1
            elif nums[i] < nums[i-1]:
                if status == 0 or status == 1:
                    count += 1
                    status = -1
        return count


a = Solution()
nums = [1,17,5,10,13,15,10,5,16,8]
print(a.wiggleMaxLength(nums))
