from collections import deque
'''
思路有一部分参考84题
主要是如何把矩阵行数转化为累计的直方图高度，然后放在同一行做面积转化
时间复杂度为O(mn)
'''
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == None or len(matrix) == 0:
            return 0
        def getMaxArea(h):
            h = [-1] + h + [-1]
            size = len(h)
            stack = deque()
            area = 0
            for i in range(size):
                while len(stack) > 0 and h[i] < h[stack[-1]]:
                    curH = h[stack.pop()]
                    while curH == h[stack[-1]]:
                        stack.pop()
                    left = stack[-1] + 1
                    right = i
                    area = max(area, (right-left)*curH)
                stack.append(i)
            return area

        m = len(matrix)
        n = len(matrix[0])
        h = [0] * n
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    h[j] = h[j] + 1
                else:
                    h[j] = 0
            #print(h)
            res = max(res, getMaxArea(h))
        return res

'''
思路二
动态规划的方法， 时间复杂度为O(m*m*n) :但是这个还是会超过时间限制
我觉得这个方法好的原因是它将所有的1换成了从左往右算有多少个连续的1
然后往上走到顶看能获得多大的面积然后替换当前面积
'''
class Solution2(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == None or len(matrix) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        wid = [[0]*n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    wid[i][j] = 0
                else:
                    if j == 0:
                        wid[i][j] = 1
                    else:
                        wid[i][j] = wid[i][j-1] + 1
                    curWid = wid[i][j]
                    '''往上遍历,如果是0就不管了'''
                    for x in range(i, -1, -1):
                        curWid = min(curWid, wid[x][j])
                        curH = i - x + 1
                        res = max(res, curWid * curH)
        return res




a  = Solution2()
m = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

print(a.maximalRectangle(m))
print("Done!")