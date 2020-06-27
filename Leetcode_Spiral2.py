class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return [[1]]
        output = [[0] * n] * n
        wholeNum = n * n
        beginNum = 0
        sumNum = (n - 1) * 4
        left = 0
        right = n
        top = 0
        bottom = n
        k = n
        margin = 0
        while (wholeNum > 0):
            # fill outer margin of matrix

            output[top][left:right] =[x for x in range(1,k+1)]
            cur = beginNum + k + 1
            for i in range(top + 1, bottom - 1):
                output[i][n - margin-1] = cur
                cur += 1
            output[bottom - 1][left:right-1] = [x for x in range(cur, cur + k + 1)][::-1]
            cur = cur + k + 1
            for i in range(bottom -2, top, -1):
                output[i][margin] = cur
                cur += 1
            top += 1
            bottom -= 1
            left += 1
            right -= 1

            wholeNum -= sumNum
            margin += 1
            k = n - 2 * margin
            sumNum = (k - 1) * 4
            if (sumNum == 0):
                sumNum = 1

        return output



class Solution2(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return[[1]]
        output = [[0]*n for _ in range(n)]
        cur = 1
        total = n * n
        left = 0
        right = n
        top = 0
        bottom = n
        while cur <= total:
            for i in range(left, right):
                output[top][i] = cur
                cur += 1
            top += 1
            for i in range(top, bottom):
                output[i][right-1] = cur
                cur += 1
            right -= 1
            for i in range(right-1, left-1, -1):
                output[bottom-1][i] = cur
                cur += 1
            bottom -= 1
            for i in range(bottom-1, top-1, -1):
                output[i][left] = cur
                cur += 1
            left += 1
        return output

if __name__ =="__main__":
    a = Solution2()
    print(a.generateMatrix(3))