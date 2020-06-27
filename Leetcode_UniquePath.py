class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if(m == 1):
            return 1
        if(n == 1):
            return 1
        else:
            downPath = self.uniquePaths(m-1, n)
            rightPath = self.uniquePaths(m, n-1)
            return downPath+rightPath

class Solution2(object):
    def uniquePaths(self, m, n):
        K = [[0]*n for _ in range(m)]
        K[0] = [1]*n
        for i in range(m):
            K[i][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                K[i][j] = K[i-1][j] + K[i][j-1]
        return K[m-1][n-1]
if __name__ == "__main__":
    a = Solution2()
    print(a.uniquePaths(23,12))