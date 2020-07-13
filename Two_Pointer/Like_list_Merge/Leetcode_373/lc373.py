import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        def get_count(value):
            top = 0
            right = len(nums2)-1
            res = 0

            while top < len(nums1) and right >= 0:
                if value > graph[top][right]:
                    res += right+1
                    top += 1
                else:
                    right -= 1
            return res

        def get_res(value,k):
            res = []
            for key in nums1:
                for val in nums2:
                    if key+val < value:
                        if len(res) >= k:
                            heapq.heappush(res, [-key-val, key, val])
                            heapq.heappop(res)
                        else:
                            heapq.heappush(res, [-key-val, key, val])
            final_res = []
            while res:
                _,i,j = heapq.heappop(res)
                final_res.append([i,j])
            return final_res
        if not nums1 or not nums2: return []
        if k >= len(nums1) * len(nums2): return [[[i,j] for j in nums2] for i in nums1]
        left = nums1[0] + nums2[0]
        right = nums1[-1] + nums2[-1]
        graph = [[nums1[i]+nums2[j] for j in range(len(nums2))] for i in range(len(nums1))]
        while left <= right:
            mid = left + (right - left) // 2
            count = get_count(mid)
            if count == k:
                return get_res(mid,k)
            elif count < k:
                left = mid+1
            else:
                right = mid-1
        return get_res(left,k)


'''
优化一下
'''

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        def get_count(value):
            top = 0
            right = len(nums2)-1
            res = 0
            res_detail = []
            while top < len(nums1) and right >= 0:
                if value > nums1[top] + nums2[right]:
                    res += right+1
                    res_detail +=[[nums1[top], nums2[i]] for i in range(right+1)]
                    top += 1
                else:
                    right -= 1
            return res, res_detail
        if not nums1 or not nums2: return []
        if k >= len(nums1) * len(nums2): return [[i,j] for i in nums1 for j in nums2]
        left = nums1[0] + nums2[0]
        right = nums1[-1] + nums2[-1]
        while left <= right:
            mid = left + (right - left) // 2
            count, res = get_count(mid)
            if count == k:
                return res
            elif count < k:
                left = mid+1
            else:
                right = mid-1
        count, res = get_count(left)
        if len(res) > k: res.sort(key=lambda item: item[0]+item[1])
        return res[:k]





a = Solution()
nums1 = [1,7,11]
nums2 =  [2,4,6]
k = 10

print(a.kSmallestPairs(nums1, nums2,k))