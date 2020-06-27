from collections import defaultdict
class Solution(object):
    def subarraysDivByK(self, A, K):
        if len(A) == 1:
            if not A[0] % K: return 1
            else: return 0
        hashmap = {}
        hashmap[0] = 1
        value = 0
        res = 0
        for i in range(len(A)):
            value += A[i]
            key = value % K
            if key in hashmap:
                res += hashmap[key]
            hashmap[key] = hashmap.get(key,0) + 1
        return res

