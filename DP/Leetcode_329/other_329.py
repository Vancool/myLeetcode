from collections import deque
class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        indegree = [[0]*n for _ in range(m)]
        zero_queue = deque()
        for i in range(m):
            for j in range(n):
                for d in direction:
                    x = i + d[0]
                    y = j + d[1]
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] < matrix[i][j]:
                        indegree[i][j] += 1
                if not indegree[i][j]:
                    zero_queue.append((i,j))
        res = 0
        while zero_queue:
            res += 1
            for _ in range(len(zero_queue)):
                i,j = zero_queue.popleft()
                for d in direction:
                    x = i + d[0]
                    y = j + d[1]
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j] and indegree[x][y] > 0:
                        indegree[x][y] -= 1
                        if not indegree[x][y]:
                            zero_queue.append((x,y))
        return res

'''
拓扑排序解法
时间复杂度 O(n*m)

当然这题也可以用记忆化 dfs的解法，时间复杂度也是 O（n*m）即我一开始写的dp
这题用dp不太好的地方在于，我不知道dp的初始状态在哪里，导致我肯定要做一次排序，要么就是从头走到尾存着看看。
如果知道了初始状态在哪里，就可以直接转化为拓扑排序BFS了， 就是从头走到尾。
'''

a = Solution()
nums = [
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]

print(a.longestIncreasingPath(nums))