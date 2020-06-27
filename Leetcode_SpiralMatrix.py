class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        x = len(matrix)
        if(x == 0):
            return matrix
        if(x == 1):
            return matrix[0]
        y = len(matrix[0])
        turnR = True
        turnL = False
        Down = False
        Up = False
        sumNum = x*y
        curx, cury = 0, 0
        WallR = y-1
        WallL = 0
        WallBottom = x-1
        WallTop = 1
        output = [matrix[curx][cury]]
        sumNum -= 1
        #print(finalX,finalY)
        while(sumNum>0):
            if(cury==WallR and turnR):
                turnR = False
                Down = True
                WallR -= 1
            if(cury==WallL and turnL):
                turnL = False
                Up = True
                WallL += 1
            if(curx==WallTop and Up):
                Up = False
                turnR =True
                WallTop += 1
            if(curx==WallBottom and Down):
                Down = False
                turnL = True
                WallBottom -= 1
            if(turnR):
                cury += 1
            if(turnL):
                cury -= 1
            if(Down):
                curx += 1
            if(Up):
                curx -= 1
            key = matrix[curx][cury]
            sumNum -= 1
            output += [matrix[curx][cury]]


        return output

if __name__ == "__main__":
    a = Solution()
    k = [[7],[9],[6]]
    print(a.spiralOrder(k))