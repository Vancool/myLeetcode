class Solution(object):
    def frequencySort(self, s):
        s = list(s)
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        bucket = [[] for _ in range(len(s)+1)]
        for key, val in freq.items():
            bucket[val].append(key)
        res = []
        for i in range(len(bucket)-1, -1,-1):
            if len(bucket[i]) > 0:
                for ch in bucket[i]:
                    res.append(ch* i)
        return ''.join(res)
'''
https://leetcode-cn.com/problems/sort-characters-by-frequency/
频率 + 桶排序
没啥好说的
'''
a = Solution()
s = "a"
print(a.frequencySort(s))