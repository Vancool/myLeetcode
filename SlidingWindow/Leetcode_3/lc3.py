class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) < 2: return len(s)
        visited = set()
        left = 0
        right = 0
        max_dis = 1

        while right < len(s):
            if s[right] not in visited:
                visited.add(s[right])
                if max_dis < right - left + 1:
                    max_dis = right - left + 1
            else:
                while s[left] != s[right]:
                    visited.remove(s[left])
                    left += 1
                left += 1
            right += 1
        return max_dis
'''
第二次写了， 题解 Interview 48
另一种方法不用remove set
哈希表的妙用，存下标
'''
class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) < 2: return len(s)
        charhash = {}
        left = 0
        right = 0
        max_dis = 1
        while right < len(s):
            if s[right] in charhash and left <= charhash[s[right]]:
                '''left每次都要往右移动 如果之前的已经弹出了left不会更改'''
                left = charhash[s[right]] + 1
            charhash[s[right]] = right
            max_dis = max(max_dis,right - left + 1)
            right += 1
        return max_dis


a = Solution1()
s = "abba"
print(a.lengthOfLongestSubstring(s))