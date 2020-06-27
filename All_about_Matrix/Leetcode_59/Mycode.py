class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==1:
            return [[1]]
        res = [[0]*n for _ in range(n)]
        stepLeftRight = [1,0,-1,0]
        stepUpDowan =[0,1,0,-1]
        direction = 0
        x = 0
        y = 0
        val = 1
        while val <= n*n:
            res[x][y] = val
            tempx = x + stepUpDowan[direction]
            tempy = y + stepLeftRight[direction]
            '''
            先试试看下一步能不能走，不能走换方向
           '''
            if tempx>=0 and tempx<n and tempy>=0 and tempy<n and res[tempx][tempy] == 0:
                x,y = tempx, tempy
            else: #change dircetion
                direction = (direction+1)%4
                x += stepUpDowan[direction]
                y += stepLeftRight[direction]
            val += 1
        return res

a = Solution()
print(a.generateMatrix(4))
print("Done!")

