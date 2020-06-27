import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.leftHeap = [] # 左边大根堆
        self.rightHeap = [] #右边小根堆


    def addNum(self, num):
        if len(self.leftHeap) == 0:
            heapq.heappush(self.leftHeap, -num)
        elif len(self.rightHeap) == 0:
            '''注意这边不能直接push，还是要和左边比较一下'''
            if -self.leftHeap[0] > num:
                heapq.heappush(self.rightHeap, -heapq.heappop(self.leftHeap))
                heapq.heappush(self.leftHeap, -num)
            else:
                heapq.heappush(self.rightHeap, num)
        else:
            if len(self.rightHeap) >= len(self.leftHeap):
                #准备左边的堆 +1 element
                if num > self.rightHeap[0]:
                    heapq.heappush(self.leftHeap, -heapq.heappop(self.rightHeap))
                    heapq.heappush(self.rightHeap, num)
                else:
                    heapq.heappush(self.leftHeap, -num)
            else:
                # 右边的堆 + 1
                if num < -self.leftHeap[0]:
                    heapq.heappush(self.rightHeap, -heapq.heappop(self.leftHeap))
                    heapq.heappush(self.leftHeap, -num)
                else:
                    heapq.heappush(self.rightHeap, num)
        '''
        add 有个更简单的写法
        如果 加到左边的堆（此时左右数量相等）我们担心右边堆顶比num更小，不然可以直接加入
            因为右边是小根堆， 可以先加到右边， 然后把右边的堆顶最小值push到左边的堆中
    同理，如果 加到右边的堆
            因为左边是大根堆，我们想让左边最大值 和 num比较一下然后大的加入到右边的堆中
            可以先把 num 加到左边， 再把左边的堆顶最大值 push到右边的堆中
        '''
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.leftHeap) == 0:
            return -1
        if len(self.leftHeap) == len(self.rightHeap):
            '''这边要注意 python2 如果负数除以二的话是向上截取
              最好换成python3 或者是其他语言
            '''
            return (-self.leftHeap[0] + self.rightHeap[0]) / 2
        else:
            return (-self.leftHeap[0])