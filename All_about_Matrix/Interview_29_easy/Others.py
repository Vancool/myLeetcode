
'''
使用方向数组来表示往前往上往下走然后来遍历，撞墙之后自己换方向

'''
class Solution:
    def spiralOrder(self, matrix):
        if not matrix:return []
        m,n = len(matrix),len(matrix[0])
        x = y = di = 0
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        res = []
        visited = set()

        for i in range(m*n):
            res.append(matrix[x][y])
            visited.add((x,y))
            nx,ny = x+dx[di],y+dy[di]
            if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited:
                x,y = nx,ny
            else:
                di = (di+1)%4  # 如果不满足条件，换一个方向进行遍历
                x,y = x+dx[di],y+dy[di]
        return res