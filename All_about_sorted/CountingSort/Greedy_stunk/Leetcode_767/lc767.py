class Solution(object):
    def reorganizeString(self, S):
        if not S: return S
        hashmap = {}
        max_set = set()
        max_val = 0
        for ch in list(S):
            hashmap[ch] = hashmap.get(ch, 0) + 1
            if max_val == hashmap[ch]: max_set.add(ch)
            if max_val < hashmap[ch]:
                max_set = set(ch)
                max_val = hashmap[ch]
        res = ""
        for _ in range(len(S)):
            tmp = sorted(hashmap, key=lambda x:hashmap[x], reverse=True)
            for key in tmp:
                if hashmap[key] > 0:
                    if len(res)>0 and res[-1] == key:
                        return ""
                    res = res + key
                    hashmap[key] -= 1
        return res
'''
这题我还是没有解出来，原来是有两种方法填
1. 按照位置奇偶来填
2. 做成大根堆按照字符频率和前一个字符关系来填

注意的是这个时候我们不知道间隔多少，所以greedy的策略是每隔一个填一次
详情见 other

'''

a = Solution()
S = "vvvlo"
print(a.reorganizeString(S))