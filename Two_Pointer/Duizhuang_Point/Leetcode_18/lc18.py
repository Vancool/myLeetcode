class Solution(object):
    def fourSum(self, nums, target):
        if not nums: return nums
        res = []
        nums.sort()
        def process(start, path, target):
            if len(path) == 4:
                if target == 0: res.append(path)
                return
            if start >= len(nums): return
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                process(i+1, path + [nums[i]], target - nums[i])
        process(0, [], target)
        return res
'''
尝试一：
暴力搜索： 超时
'''
'''
尝试二： 
组合 + 双指针
'''
class Solution(object):
    def fourSum(self, nums, target):
        if not nums: return nums
        if len(nums) < 4: return []
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]: continue
                left = j+1
                right = len(nums) - 1
                while left < right:
                    value = nums[left] + nums[right] + nums[i] + nums[j]
                    if value == target:
                        res.append([nums[left], nums[right], nums[i], nums[j]])
                        left += 1
                        right -= 1
                        while right > left > j + 1 and nums[left] == nums[left-1]:
                            left += 1
                        while left < right < len(nums)-1 and nums[right] == nums[right+1]:
                            right -= 1
                    elif value > target:
                        right -= 1
                    elif value < target:
                        left += 1
        return res

'''
还可以用一个哈希表存着 两两值的数组，然后转化为哈希表求两数之和
但是这个很麻烦，而且效率不高
'''


a = Solution()
nums = [4,-9,-2,-2,-7,9,9,5,10,-10,4,5,2,-4,-2,4,-9,5]
print(a.fourSum(nums, -13))