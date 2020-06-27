from collections import defaultdict
from collections import  Counter
class Solution(object):
    def minWindow(self, s, t):
        if len(s) < len(t): return ""
        if t in s: return t
        dic = defaultdict(list)
        tset = Counter(t)
        for i in range(len(s)):
            if s[i] in tset:
                dic[s[i]].append(i)
        for key in dic.keys():
            if len(dic[key]) < tset[key]:
                return ""
        self.min_dis = float('inf')
        self.min_left = -1
        self.min_right = -1
        path = set()
        def get_min(index, path):
            if index == len(t):
                left = min(path)
                right = max(path)
                if right - left + 1 < self.min_dis:
                    self.min_dis = right - left + 1
                    self.min_right = right
                    self.min_left = left
                return
            for num in dic[t[index]]:
                if num not in path:
                    path.add(num)
                    get_min(index+1, path)
                    path.remove(num)
        get_min(0, path)
        return s[self.min_left: self.min_right+1]
'''
这题没做出来
硬着用枚举超时了，其实关于max(index) - min(index) 的问题可以用滑动窗口剪枝
这样每个哈希的位置最多只要用2次， 比枚举的迭代次数少了很多
'''
a = Solution()
S = "ADOBECODEBANC"
T = "AA"
print(a.minWindow(S, T))
print("Done")

