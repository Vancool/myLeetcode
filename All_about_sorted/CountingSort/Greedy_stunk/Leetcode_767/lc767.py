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


a = Solution()
S = "vvvlo"
print(a.reorganizeString(S))