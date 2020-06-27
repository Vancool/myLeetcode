class Solution(object):
    def combinationSum2(self, candidates, target):
        if len(candidates) * target == 0: return []
        if len(candidates) == 1: return [candidates] if candidates[0] == target else[]
        candidates.sort()
        res = []
        def backtrack(index, target, path):
            if target == 0:
                res.append(list(path))
                return
            for i in range(index, len(candidates)):
                if target - candidates[i] < 0:
                    break
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                backtrack(i+1, target - candidates[i], path + [candidates[i]])
        backtrack(0, target, [])
        return res
'''
回溯，去重
https://leetcode-cn.com/problems/combination-sum-ii/
'''
a = Solution()
can = [2,5,2,1,2,2]
t = 8
print(a.combinationSum2(can, t))
print("Done")