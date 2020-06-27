class Solution(object):
    def findTheLongestSubstring(self, s):
        if len(s) == 0: return 0
        hashmap = [-1] * 32
        '''
        需要注意的是 0状态其实在空字符串已经出现了，所以
        hashmap[0] = 0
        而 hash[status] = i ， i 是指第i个字符
        '''
        hashmap[0] = 0
        cur = 0
        i = 0
        res = 1
        for str in s:
            if str == 'a':
                cur ^= 1
            elif str == 'e':
                cur ^= 1<<1
            elif str == 'i':
                cur ^= 1<<2
            elif str == 'o':
                cur ^= 1<<3
            elif str == 'u':
                cur ^= 1 << 4
            if hashmap[cur] == -1: hashmap[cur] = i+1
            else:
                res = max(res, i+1 - hashmap[cur])
            i += 1
        return res
a = Solution()
print(a.findTheLongestSubstring("eleetminicoworoep"))




'''
这题真的好难， 我完全不会
使用的是前缀和 + 状态压缩
注意前缀和不需要注意前后顺序的，以后遇到字串状态 或者 字串和 可以考虑用前缀
统计一下 [0:i] 字符的个数， 然后看[i,j]段（[0:j]-[0:i]）是否是偶数
本来应该用 O(N^2)算一下 所有字串[i,j]段的是否是偶数，但是因为已经知道了每一格可能出现的状态
是否有a o e i u 
所以最多可能会出现 2^5 个状态
然后这个时候可以用一个哈希表存着最早出现这个状态的字符串
但是因为是偶数的字符所以每个字符可以用一个位来表示状态压缩存储
'''
