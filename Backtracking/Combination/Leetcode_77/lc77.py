class Solution(object):
    def combine(self, n, k):
        if k == 0 or k > n: return []
        if k == n: return [[key for key in range(1, n+1)]]
        if k == 1: return [[key] for key in range(1, n+1)]
        res = []
        num = [i for i in range(1, n+1)]
        def dfs(path, k):
            if k == 0:
                res.append(list(path))
            for i in range(n):
                if num[i] != 0 and(len(path) == 0 or path[-1] < num[i]):
                    tmp = num[i]
                    path.append(tmp)
                    num[i] = 0
                    dfs(path, k-1)
                    path.pop()
                    num[i] = tmp
        dfs([], k)
        return res
'''
简洁一点：
'''
class Solution(object):
    def combine(self, n, k):
        if k == 0 or k > n: return []
        if k == n: return [[key for key in range(1, n+1)]]
        if k == 1: return [[key] for key in range(1, n+1)]
        res = []
        def backtrack(path, index, n, k):
            if index > n+1:
                return
            if k == 0:
                res.append(path)
                return
            for i in range(index, n+1):
                backtrack(path + [i], i+1, n, k-1)

        backtrack([], 1,n, k)
        return res

'''
巧用组合性质：
C(m,n)=C(m-1,n)+C(m-1,n-1)
'''
class Solution(object):
    def combine(self, n, k):
        memoMap = {}
        def Process(n, k):
            if (n, k) in memoMap:
                return memoMap[(n,k)]
            if k > n or k == 0:
                memoMap[(n,k)] = []
                return []
            if k == 1:
                memoMap[(n, k)] = [[i] for i in range(1, n + 1)]
                return memoMap[(n, k)]
            if k == n:
                memoMap[(n, k)] = [[i for i in range(1, n + 1)]]
                return memoMap[(n, k)]

            answer = Process(n - 1, k)
            for item in Process(n - 1, k - 1):
                item.append(n)
                answer.append(list(item))
                item.pop()
            memoMap[(n,k)] = answer
            return answer
        return Process(n,k)
a = Solution()
print(a.combine(5,3))
print("Done")


