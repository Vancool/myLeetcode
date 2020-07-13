class Solution(object):
    def kthSmallest(self, matrix, k):
        def get_count(value):
            res = 0
            l = 0
            r = len(matrix)-1
            while l < len(matrix) and r >= 0:
                if matrix[l][r] <= value: # 这边是等于号， 要注意
                    res += r+1 # 这边要注意 res 是数量
                    l += 1
                else:
                    r -= 1
            return res
        left = matrix[0][0]
        right = matrix[len(matrix)-1][len(matrix)-1]
        while left < right:
            mid = left + (right-left)//2
            res = get_count(mid)
            if res < k:
                left = mid+1
            else:
                right = mid
        return right

'''
堆解法
'''
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        min_heap = [(matrix[i][0], i,0) for i in range(len(matrix))]
        heapq.heapify(min_heap)
        while k > 0:
            value, idx, i = heapq.heappop(min_heap)
            if i < len(matrix)-1:
                heapq.heappush(min_heap, (matrix[idx][i+1],idx,i+1))
            k -= 1
        return value



a = Solution()
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
print(a.kthSmallest(matrix, k))
