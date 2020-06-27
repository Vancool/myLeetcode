'''
看到排序好的数组，常规写法二分法找元素
此处是横纵都用二分法
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        def twoBinarySearch(matrix, x, y, target, is_row):
            if is_row:
                start = y
                end = len(matrix[0]) - 1
                if start > end or matrix[x][start] > target or matrix[x][end] < target:
                    return False
                if start == end:
                    return target == matrix[x][start]
                while start <= end:
                    mid = (start + end) // 2
                    if matrix[x][mid] > target:
                        end = mid - 1
                    elif matrix[x][mid] < target:
                        start = mid + 1
                    else:
                        return True
            else:
                start = x
                end = len(matrix) - 1
                if start > end or  matrix[start][y] > target or matrix[end][y] < target:
                    return False
                if start == end:
                    return target == matrix[start][y]
                while start <= end:
                    mid = (start + end) // 2
                    if matrix[mid][y] > target:
                        end = mid - 1
                    elif matrix[mid][y] < target:
                        start = mid + 1
                    else:
                        return True
            return False

        if matrix == None or len(matrix) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        t = min(m, n)
        for i in range(t):
            rowVal = twoBinarySearch(matrix, i, i, target, True)
            colVal = twoBinarySearch(matrix, i + 1, i, target, False)
            if rowVal or colVal:
                return True
        return False


a = Solution()
m = [[1],[3],[5]]
print(a.searchMatrix(m,0))
print("Done!")

