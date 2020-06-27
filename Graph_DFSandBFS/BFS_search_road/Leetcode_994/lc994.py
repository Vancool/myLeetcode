from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        queue = deque()
        or_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    grid[i][j] = 0
                    or_count += 1
                if grid[i][j] == 1:
                    or_count += 1
        if or_count == 0: return 0
        res = -1
        while queue:
            res += 1
            for _ in range(len(queue)):
                pos = queue.popleft()
                or_count -= 1
                for direct in direction:
                    x = pos[0] + direct[0]
                    y = pos[1] - direct[1]
                    if 0<=x<m and 0<=y<n and grid[x][y]:
                            queue.append((x, y))
                            grid[x][y] = 0
        return res if or_count == 0 else -1





a = Solution()
grid = [[0]]
print(a.orangesRotting(grid))


