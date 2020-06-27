import heapq
'''
两个方法，一种是用堆来做，时间复杂度为O(nlog(n))
另一种是用动态规划三指针来做，时间复杂度是O(n)
我个人推荐用动态规划来做，但是比较难想出来原来是用三指针动态规划
'''
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        has_seen = set()
        has_seen.add(1)
        heap = []
        heapq.heappush(heap, 1)
        count = 1
        key = [2,3,5]
        while count < n:
            val = heapq.heappop(heap)
            count += 1
            for k in key:
                res = k * val
                if res not in has_seen:
                    has_seen.add(res)
                    heapq.heappush(heap, res)
        return heapq.heappop(heap)

class Solution2(object):
    def nthUglyNumber(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        res = [1]
        index2=index3=index5 = 0
        count = 1
        while count < n:
            val2 = res[index2] * 2
            val3 = res[index3] * 3
            val5 = res[index5] * 5
            val = min(val2,min(val3,val5))
            '''
            注意这个地方一定是if而不是elseif
            因为3*5和5*3是同时成为min
            （如果不同时说明中间有一个数，但是我们已经限定了是递增数列）
            因此这个时候要 index5+1 和 index3+1
            不然就会加到重复的数
            '''
            if val == val2:
                index2 += 1
            if val == val3:
                index3 += 1
            if val == val5:
                index5 += 1
            count += 1
            res.append(val)
        return res[-1]



a = Solution()
n = 10
print(a.nthUglyNumber(10))