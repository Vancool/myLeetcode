class Solution(object):
    def combinationSum(self, candidates, target):
        if len(candidates)* target == 0: return []
        #if len(candidates) == 1: return [] if target != candidates[0] else [candidates[0]]
        '''
        这个判断不行， 比如test case
        [1] 2 
        '''
        res = []
        candidates.sort()
        if target < candidates[0] : return []
        def backtrack(path, target):
            if target == 0:
                res.append(list(path))
                return
            for key in candidates:
                if target < key:
                    break
                if len(path) == 0 or key >= path[-1]:
                    backtrack(path + [key], target-key)
        backtrack([], target)
        return res
'''
更加简洁的模板
'''
class Solution(object):
    def combinationSum(self, candidates, target):
        if len(candidates)* target == 0: return []
        res = []
        candidates.sort()
        def backtrack(index, path, target):
            if target < 0:
                return
            if target == 0:
                res.append(list(path))
                return
            for i in range(index, len(candidates)):
                if target - candidates[i] < 0:
                    break
                backtrack(i, path + [candidates[i]], target - candidates[i])
        backtrack(0,[], target)
        return res
a = Solution()
candidates = [2, 3,5]
target = 8
print(a.combinationSum(candidates, target))
print("Done")


