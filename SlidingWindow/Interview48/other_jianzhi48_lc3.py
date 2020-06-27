class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {}
        '''
        双指针+hashmap做滑动窗口题
        hashmap存下标的妙用
        如果是求出字符那么有用queue
        '''
        head, res = 0,0
        for i in range(len(s)):
            if s[i] in hashmap:
                head = max(hashmap[s[i]]+1, head) #start from where
            hashmap[s[i]] = i
            res = max(res, i-head+1)
        return res
