import heapq
class Solution(object):
    def nthUglyNumber(self, n):
         res = set()
         min_heap = [1]
         while len(res) < n:
             val = heapq.heappop(min_heap)
             res.add(val)
             for key in [2,3,5]:
                 heapq.heappush(min_heap, val*key)
         return val

'''
尝试一： 超时
attention: 
1. 记得要去重， 重复 value
2. 只返回最后一个，而不是一个列表
3. 去重方式可以用set, 或者最小堆里面去掉下一个有重复的
'''
'''
用set的去重方法：
'''
import heapq
class Solution(object):
    def nthUglyNumber(self, n):
         min_heap = [1]
         while n:
             val = heapq.heappop(min_heap)
             n -= 1
             while len(min_heap)>0 and val == min_heap[0]:
                 heapq.heappop(min_heap)
             for key in [2,3,5]:
                 heapq.heappush(min_heap, val*key)
         return val

'''
时间复杂度为 O(nlog(n))
超过了 8% 慢到离谱
'''


class Solution(object):
    def nthUglyNumber(self, n):
        res = [1]
        two_point = 0
        three_point = 0
        five_point = 0
        while n > 1:
            two = res[two_point] * 2
            three = res[three_point] * 3
            five = res[five_point] * 5
            res.append(min(two, three, five))
            n -= 1
            if res[-1] == two:
                two_point += 1
            if res[-1] == three:
                three_point += 1
            if res[-1] == five:
                five_point += 1
        return res[-1]

'''
做成离线存储的形式会更好：
'''
class Ugly:
    def __init__(self):
        self.nums = nums = [1, ]
        i2 = i3 = i5 = 0
        for i in range(1, 1690):
            ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(ugly)

            if ugly == nums[i2] * 2:
                i2 += 1
            if ugly == nums[i3] * 3:
                i3 += 1
            if ugly == nums[i5] * 5:
                i5 += 1
class Solution:
    u = Ugly()
    def nthUglyNumber(self, n):
        return self.u.nums[n - 1]


a = Solution()
print(a.nthUglyNumber(10))