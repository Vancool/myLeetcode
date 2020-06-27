class Solution(object):
    def combinationSum3(self, k, n):
        if n <= 1 * k or n >= 9 * k or k == 0: return []
        if k == 1: return [[n]]
        res = []
        def backtrack(index, k, n, path):
            if n == 0:
                if k ==0:
                    res.append(list(path))
                return
            if k == 0:
                return
            for i in range(index, 10):
                if i > n: break
                backtrack(i+1, k-1, n-i, path + [i])
        backtrack(1,k, n, [])
        return res

'''
可以考虑多加一步剪枝：
        // 寻找 n 的上限：[9, 8, ... , (9 - k + 1)]，它们的和为 (19 - k) * k / 2
        // 比上限还大，就不用搜索了：
        if (n > (19 - k) * k / 2) {
            return res;
        }
        
        下限：
        10 - start < k: return 
        如果 [start, 9] 都不够k个，直接不用搜了

'''
a = Solution()
print(a.combinationSum3(2,4))
print("Done")