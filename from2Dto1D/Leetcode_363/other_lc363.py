import bisect
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        def get_max_val(row_res):
            '''这部分是 Leetcode 53 最大子序列和的解法：'''
            res = -float("inf")
            cur = 0
            for i in range(len(row_res)):
                res = max(res, cur+row_res[i])
                cur = max(cur+row_res[i], 0)
            return res
        res = -float('inf')
        col_num = len(matrix[0])
        for i in range(col_num):
            row_res = [0] * len(matrix)
            for j in range(i, col_num):
                row_res = [row_res[row]+matrix[row][j] for row in range(len(matrix))]
                max_row_res = get_max_val(row_res)
                if max_row_res == k: return k
                if max_row_res < k:
                    res = max(max_row_res, res)
                    continue
                # binary search max value of the area
                # start with count the premix sum
                # premix = [0]
                # cur_premix = 0
                # for row_r in row_res:
                #     cur_premix += row_r
                #     idx = bisect.bisect_left(premix, cur_premix-k)
                #     if idx < len(premix) and cur_premix - premix[idx] <= k:
                #         res = max(res, cur_premix - premix[idx])
                #     bisect.insort_left(premix, cur_premix)
                '''
                不用前缀和二分法， 直接暴力求解更好
                '''
                for left in range(len(row_res)):
                    sm = 0
                    for right in range(left, len(row_res)):
                        sm += row_res[right]
                        if sm > res and sm <= k:
                            res = sm
                if res == k: return res
        return res

a = Solution()
matrix = [[2,2,-1]]
k = 0
print(a.maxSumSubmatrix(matrix, k))

'''
bisect_left 用法： 查找效率 O(log(N))
                  是会返回第一个找到的值的下标， 如果没找到就返回最后一个比它小的下标的下一个
                  和right的区别是 right找到之后会返回最后一个找到的下标的下一个
                  
bisect isort的时间复杂度为 O(n)
-----------------------------------------------------------------------------------------
另外需要注意的是这个最小值不是0， 所以初始化的时候要将所有的res 初始为 -float('inf')
'''


