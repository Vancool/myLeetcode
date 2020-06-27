class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        diff = float("inf")
        res = float("inf")
        for i in range(len(nums)):
            # 加个去重可以优化效率
            if i > 0 and nums[i] == nums[i-1]:
                continue
            cur_target = target - nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                cur_value = nums[left] + nums[right]
                if cur_value < cur_target:
                    left += 1
                elif cur_value > cur_target:
                    right -= 1
                else:
                    return target
                if abs(nums[i]+cur_value-target) < diff:
                    res = nums[i]+cur_value
                    diff = abs(res-target)
        return res
'''
可以再继续加边界的优化，求出最大和最小直接得到差距
但是要重复写，这边就不写了
'''

a = Solution()
nums = nums = [-1,2,1,-4]
target = 1
print(a.threeSumClosest(nums, target))


