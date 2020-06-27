import heapq
class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        if len(arr) <= k:
            return arr
        res = []
        for num in arr:
            if len(res) < k:
                heapq.heappush(res, -num)
            else:
                n = min(num, -heapq.heappop(res))
                heapq.heappush(res,-n)
        res = [-num for num in res]
        return res

a = Solution()
arr = [3,2,1]
k = 2
print(a.getLeastNumbers(arr, k))
print("Done!")
