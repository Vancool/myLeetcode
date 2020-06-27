import heapq
class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = [] #大顶堆，存小于中位数的值
        self.maxHeap = []
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.minHeap) == 0:
            heapq.heappush(self.minHeap, -num)
        elif len(self.minHeap) > len(self.maxHeap):
            if -self.minHeap[0] <= num:
                heapq.heappush(self.maxHeap, num)
            else:
                temp = -heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, -num)
                heapq.heappush(self.maxHeap, temp)
        else:
            if num <= self.maxHeap[0]:
                heapq.heappush(self.minHeap, -num)
            else:
                temp = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, -temp)
                heapq.heappush(self.maxHeap, num)



    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.minHeap) == len(self.maxHeap):
            return (-self.minHeap[0]+self.maxHeap[0])/2
        else:
            return -self.minHeap[0]


obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(3)
param_2 = obj.findMedian()
print(param_2)