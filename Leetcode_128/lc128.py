class Solution(object):
    def longestConsecutive(self, nums):
        hashmap = set(nums)
        max_count = [nums]
        while True:
            res = []
            for key in max_count[-1]:
                if key+1 in hashmap:
                    res.append(key+1)
            if res == []: break
            max_count.append(res)
        return len(max_count)
'''
超时
'''
'''
哈希表记忆深度搜索
'''
class Solution(object):
    def longestConsecutive(self, nums):
        hashmap = {}
        nums_set = set(nums)
        def dfs(nextvalue):
            if nextvalue in hashmap:
                return hashmap[nextvalue]
            res = 0
            if nextvalue in nums_set:
                res = dfs(nextvalue+1)+1
                hashmap[nextvalue] = res
            return res
        res = 1
        for i in range(len(nums)):
            res = max(res,dfs(nums[i]))
        return res
'''
迭代模拟搜索
'''
class Solution(object):
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        res = 0
        for num in nums:
            if num-1 in nums_set: continue
            count = 1
            while num+1 in nums_set:
                num = num + 1
                count += 1
            res = max(count, res)
        return res

'''
并查集
'''

a = Solution()
nums = [100,4,200,1,3,2]
print(a.longestConsecutive(nums))