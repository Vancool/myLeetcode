from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid),len(grid[0])
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1
        if m == 1 and n == 1: #不加这个if最后会返回-1
            return 1
        direction = [[1,1],[0,1],[1,0],[-1,1],[1,-1],[-1,0],[0,-1]]
        #因为不走回头路，所以不算肯定会走过的路比如[-1,-1],如果它是0的话一定会在hash中的
        queue = deque()
        has_visited = set()
        res = 0
        queue.append((0,0))
        has_visited.add((0,0))

        while queue:
            res += 1
            num = len(queue)
            for i in range(num):
                start = queue.popleft()
                for step in direction:
                    dx = start[0] + step[0]
                    dy = start[1] + step[1]
                    if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] == 0 and (dx, dy) not in has_visited:
                        if dx  == m-1 and dy == n-1:
                            return res + 1
                            '''如果找到了一定会返回，如果找不到一定会跳出循环'''
                        queue.append((dx, dy))
                        has_visited.add((dx, dy))
        return -1






'''
BFS练习
试一下能不能用DFS加上优先级来做(不行
试了一下能不能用dp做，也可以，但是想法就不同了
先把grid为1的改成 inf 不可达
然后转移方程为 min(看到的坐标) + 1
返回值是 dp[m-1][n-1] 如果是inf 就是-1， 如果是正常值就是1
但是这样的话循环里面也不是正常的从左到右从上到下，而是每次的广度优先搜索
所以还是用广度优先搜索会更好
'''

'''
test case:
1.
[[0]]
2.
[[0,0]]
3.
[[0,1],[1,0]]
4.
这个test case 没注意到
有可能走不通的
[[0,0],[0,1]]
5.
[[0,0,1],
 [0,1,1],
 [0,0,0]]
'''
a =Solution()
grid = [[0,0,1],
 [0,1,1],
 [0,0,0]]
print(a.shortestPathBinaryMatrix(grid))
print("Done")

