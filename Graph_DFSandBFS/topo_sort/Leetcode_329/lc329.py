import heapq
class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        min_heap = []
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        graph = [[1]*n for _ in range(m)]
        res = 1
        for i in range(m):
            for j in range(n):
                min_heap.append((matrix[i][j],i,j))
        heapq.heapify(min_heap)
        while min_heap:
            val, x, y = heapq.heappop(min_heap)
            for d in direction:
                ix = d[0] + x
                iy = d[1] + y
                if 0 <= ix < m and 0 <= iy < n and val > matrix[ix][iy]:
                    graph[x][y] = max(graph[x][y],graph[ix][iy]+1)
                res = max(graph[x][y], res)
        return res

'''
想到了用dp, 以为用个堆每次找最小的就好，没想到可以把它看成图的dp, 做一个拓扑排序
标准答案在others
'''

a = Solution()
nums = [
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]

print(a.longestIncreasingPath(nums))

