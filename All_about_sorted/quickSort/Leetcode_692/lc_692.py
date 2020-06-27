import heapq
from collections import Counter,deque
class key_val():
    def __init__(self, key, val):
        self.key = key
        self.val = val
    def __gt__(self, other):
        if self.val > other.val:
            return True
        elif self.val == other.val:
            return self.key < other.key
        return False

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        if len(words) == 0 or k == 0:
            return  []
        dic = Counter(words)
        heap = []
        for key, val in dic.items():
            heapq.heappush(heap, key_val(key, val))
            if len(heap) > k:
                heapq.heappop(heap)
        res = deque()
        for _ in range(k):
            res.appendleft(heapq.heappop(heap).key)
        return res
a = Solution()
s = ["i", "love", "leetcode", "i", "love", "coding"]
print(a.topKFrequent(s, 4))
print("Done")



