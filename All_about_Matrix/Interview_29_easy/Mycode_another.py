class Solution(object):
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        res = []
        m = len(matrix)
        n = len(matrix[0])
        def getOutside(matrix, left, right, up, down, res):
            if up == down:
                for i in range(left, right+1):
                    res.append(matrix[up][i])
            elif left == right:
                for i in range(up, down+1):
                    res.append(matrix[i][left])
            else:
                for j in range(left, right+1):
                    res.append(matrix[up][j])
                for i in range(up+1, down+1):
                    res.append(matrix[i][right])
                for j in range(right-1, left-1,-1):
                    res.append(matrix[down][j])
                for i in range(down-1,up, -1):
                    res.append(matrix[i][left])
                up += 1
                down -= 1
                left += 1
                right -= 1
                if up <= down and left <= right:
                    getOutside(matrix,left,right,up, down, res)
        getOutside(matrix,0,n-1,0,m-1,res)
        return res


if __name__ == "__main__":
    m = [[1]]
    a = Solution()
    print(a.spiralOrder(m))
    print("Done")

