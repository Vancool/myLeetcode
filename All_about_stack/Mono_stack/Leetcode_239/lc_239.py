import heapq
class num_idx():
    def __init__(self, num, idx):
        self.num = num
        self.index = idx
    def __gt__(self, other):
        return self.num > other.num
    '''
    我自己写的时候用了堆，然后顺便存了一个index来去掉左边
    这样就可以每次都找到最大值
    但是其实可以维护一个单调栈来做
       
       '''
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        if k == 1:
            return nums
        if k == len(nums):
            return [max(nums)]
        heap = []
        i = 0
        while len(heap) < k:
            heapq.heappush(heap, num_idx(-nums[i], i))
            i += 1
        res.append(-heap[0].num)
        left = 0
        for i in range(k, len(nums)):
            if -heap[0].num == nums[left]:
                heapq.heappop(heap)
                while heap[0].index < left:
                    heapq.heappop(heap)
            heapq.heappush(heap, num_idx(-nums[i], i))
            res.append(-heap[0].num)
            left += 1
        return res

a = Solution()
num = [1,3,-1,-3,5,3,6,7]
print(a.maxSlidingWindow(num,3))
print("Done")





