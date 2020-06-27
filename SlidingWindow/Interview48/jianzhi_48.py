from collections import deque
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        res, cur = 0,0
        has_seen = set()
        queue = deque()
        for key in s:
            if key not in has_seen:
                cur += 1
                res = max(res, cur)
                has_seen.add(key)
                queue.append(key)
            else:
                while queue[0] != key:
                    ch = queue.popleft()
                    has_seen.remove(ch)
                    cur -= 1
                queue.popleft()
                queue.append(key)
                res = max(res, cur)
        return res
a = Solution()
s = "abcabcbb"
print(a.lengthOfLongestSubstring(s))
print("Done")