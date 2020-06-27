class Solution1(object):
    def combinationSum4(self, nums, target):
        if len(nums) * target == 0: return []
        nums.sort()
        res = []

        def backtrack(target, path):
            if target == 0:
                res.append(list(path))
                return
            for i in range(len(nums)):
                if nums[i] > target: break
                backtrack(target - nums[i], path + [nums[i]])

        backtrack(target, [])
        return len(res)
'''
回溯超时， 复杂度为 O(N ^ target)
'''
'''
试一下记忆递归
'''
class Solution(object):
    def combinationSum4(self, nums, target):
        if len(nums) * target == 0: return 0
        memohash = {}
        nums.sort()
        memohash[0] = 1
        def dfs(target):
            if target in memohash:
                return memohash[target]
            res = 0
            for i in range(len(nums)):
                if nums[i] > target:
                    break
                res += dfs(target - nums[i])
            memohash[target] = res
            return res
        return dfs(target)






a = Solution()
nums = [1,2,3,4]
print(a.combinationSum4(nums, 4))
print("Done")