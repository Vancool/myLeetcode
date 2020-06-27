class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return []
        n = len(matrix)
        def myRotate(start, outsideIndex,matrix):
            if outsideIndex == 1 or outsideIndex == 0:
                return
            for i in range(start,start+outsideIndex-1):
                x = start
                y = i
                temp1 = matrix[x][y]
                for j in range(4):
                    x, y = y, 2*start+outsideIndex - 1  - x
                    temp2 = matrix[x][y]
                    matrix[x][y] = temp1
                    temp1 = temp2
            myRotate(start+1, outsideIndex-2, matrix)
        myRotate(0,n,matrix)
        return matrix

a = Solution()
k = a.rotate([
    [1,2,3,4,5],
  [ 5, 1, 9,11,1],
  [ 2, 4, 8,10,2],
  [13, 3, 6, 7,3],
  [15,14,12,16,4]
])
print(k)
print("Done!")


