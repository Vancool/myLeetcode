from collections import  deque

'''实际上这题用深搜和广搜会更好写一些'''

class Solution(object):
    def movingCount(self, m, n, k):
        if k == 0:
            return 1
        def validStep(x,y, key):
            val = 0
            while x:
                val += x%10
                x = x //10
            while y:
                val += y%10
                y = y // 10
            return val <= key
        count = 1
        step =[(0,1)(1,0)]
        queue = deque()
        queue.append((0,0))
        visited = set()
        visited.add((0,0))
        while queue:
            x, y = queue.popleft()
            for dx, dy in step:
                curx = x+dx
                cury = y+dy
                if 0<= curx< m and 0<= cury < n and\
                        validStep(curx,cury, k) and\
                        (curx, cury) not in visited:
                    visited.add(curx,cury)
                    queue.append(curx,cury)
                    count += 1
        return count