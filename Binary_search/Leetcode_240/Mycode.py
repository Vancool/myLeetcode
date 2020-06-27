'''
这题没写出来

'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0:
            return False
        def findElement(mStart, nStart,newMatrix, target):
            m = len(newMatrix)
            n = len(newMatrix[0])
            if matrix[m-1][n-1] <target:
                return False
            if mStart == m-1:
                for i in range(nStart, n):
                    if newMatrix[mStart][i] == target:
                        return True
                return False
            if nStart == n-1:
                for i in range(mStart, m):
                    if newMatrix[i][nStart] == target:
                        return True
                return False
            x = mStart
            y = nStart
            while x<m and y<n:
                if matrix[x][y] >= target:
                    break
                x += 1
                y += 1

            if x<m and y<n:
                for i in range(nStart, y+1):
                    if matrix[x][i] == target:
                        return True
                    elif matrix[x][i] > target:
                        break
                for i in range(mStart, x+1):
                    if matrix[i][y] == target:
                        return True
                    elif matrix[i][y] > target:
                        break
                return False
            else:
                if x == m:
                    if nStart+m > n:
                        mStart = (n-m) + mStart
                    else:
                        nStart = nStart + m
                elif y == n:
                    if mStart+n > m:
                        nStart = nStart + (m-n)
                    else:
                        mStart = mStart + n
                return findElement(mStart, nStart, newMatrix,target)

        return findElement(0,0,matrix,target)

a = Solution()
m = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22]
]
k = a.searchMatrix(m,16)
print(k)
print("Done")
