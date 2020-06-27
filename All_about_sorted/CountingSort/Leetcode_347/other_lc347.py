from collections import defaultdict
'''
个人建议是直接用带随机的快排做 可以达到O(n)的时间复杂度
但是题解中给出了
涉及到频率问题还是用 哈希表 + 计数排序 会更好
因为频率是确定的由 0-n, 桶里面装key
时间复杂度是O(n） 空间复杂度是O(n)
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        tank = [ [] for _ in range(len(nums)+1)]
        for key, val in freq.items():
            tank[val].append(key)
        res = []
        for t in tank[::-1]:
            if len(t) > 0:
                for elem in t:
                    res.append(elem)
                    if len(res) == k:
                        return res

