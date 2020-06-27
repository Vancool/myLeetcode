class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        m = len(matrix)
        n = len(matrix[0])
        res = []
        i = 0
        j = 0
        x = 0
        y = 0
        while i <= (m-1)//2 and j <= (n-1)//2:
            x = i
            for y in range(j,n-j): #turn right
                res.append(matrix[x][y])
            if i+1 >= m-i:
                break
            for x in range(i+1,m-i):#turn down
                res.append(matrix[x][y])
            if n-j-2<=j-1:
                break
            for y in range(n-j-2,j-1,-1):
                res.append(matrix[x][y])
            if i>=m-i-2:
                break
            for x in range(m-i-2, i, -1):
                res.append(matrix[x][y])
            i += 1
            j += 1
        return res


class Solution2(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        visited = set()
        step = [(0, 1),(1, 0), (0, -1),  (-1, 0)]
        direction = 0
        res = []
        res.append(matrix[0][0])
        visited.add((0, 0))
        i = 0
        j = 0
        while len(res) < m * n:
            dx = i + step[direction][0]
            dy = j + step[direction][1]
            if 0 <= dx < m and 0 <= dy < n and (dx, dy) not in visited:

                visited.add((dx, dy))
                res.append(matrix[dx][dy])
                i = dx
                j = dy
            else:
                direction = (direction + 1) % 4
        return res
if __name__ == "__main__":
    m = [[1,2,3],[4,5,6],[7,8,9]]
    a = Solution2()
    print(a.spiralOrder(m))
    print("Done")