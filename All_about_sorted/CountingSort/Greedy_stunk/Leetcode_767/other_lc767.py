class Solution(object):
    def reorganizeString(self, S):
        if not S: return S
        hashmap = [0] * 26
        max_idx = 0
        S = list(S)
        for ch in S:
            idx = ord(ch) - ord('a')
            hashmap[idx] = hashmap[idx] + 1
            if (hashmap[idx]-(len(S)-hashmap[idx])) > 1: return ""
            if hashmap[max_idx] < hashmap[idx]:
                max_idx = idx
        idx = 0
        '''
        如果最大的频率是奇数， 就需要先放，不然可能会有贴在一起的情况， 比如
        会出现 vvvab [a v b v v ]
        这个有两种解决方式：
        1. 先处理最大频率
        2. 先将哈希表存在大根堆里一个一个弹出
        3. 在最大频率为 len//2+1 的时候特定只存在奇数的位置， 然后先存偶数
        即这个解法
        https://leetcode-cn.com/problems/reorganize-string/solution/zui-you-jie-fa-tong-guo-by-18520397110-2/
        '''
        while hashmap[max_idx]:
            S[idx] = chr(max_idx + ord('a'))
            hashmap[max_idx] -= 1
            idx += 2
        for i in range(26):
            while hashmap[i] > 0:
                if idx >= len(S): idx = 1
                S[idx] = chr(i+ord('a'))
                hashmap[i] -= 1
                idx += 2
        return "".join(S)

a = Solution()
S = "vvvab"
print(a.reorganizeString(S))