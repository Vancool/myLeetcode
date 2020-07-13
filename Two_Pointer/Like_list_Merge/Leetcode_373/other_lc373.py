import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2: return []
        if k >= len(nums1) * len(nums2): return [[i,j] for i in nums1 for j in nums2]
        flag = True
        if len(nums1) > len(nums2):
            flag = False
            nums1,nums2 = nums2, nums1
        min_heap = []
        for i in range(len(nums1)):
            heapq.heappush(min_heap, [nums1[i]+nums2[0],i,0])
        res = []
        while len(res) < k:
            val, x, y = heapq.heappop(min_heap)
            if flag:
                res.append([nums1[x], nums2[y]])
            else:
                res.append([nums2[y], nums1[x]])
            if y+1 < len(nums2):
                heapq.heappush(min_heap, [nums2[y+1]+nums1[x], x, y+1])
        return res
'''
这个还是慢了一些
另一种写法
'''
import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2: return []
        if k >= len(nums1) * len(nums2): return [[i,j] for i in nums1 for j in nums2]
        min_heap = [[nums1[0]+nums2[0],0,0]]
        res = []
        while k > 0:
            _, x, y = heapq.heappop(min_heap)
            res.append([nums1[x], nums2[y]])
            k -= 1
            if x == 0 and y<len(nums2)-1:
                heapq.heappush(min_heap, [nums1[x]+nums2[y+1], x, y+1])
            x += 1
            if x < len(nums1):
                heapq.heappush(min_heap, [nums1[x]+nums2[y], x, y])
        return res
a = Solution()
nums1 = [1,7,11]
nums2 =  [2,4,6]
k = 3

print(a.kSmallestPairs(nums1, nums2,k))
