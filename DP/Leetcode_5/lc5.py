class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0 or len(s) == 1:
            return s
        if len(s) == 2:
            return "" if s[0] != s[1] else s
        resLeft = 0
        resRight = 0
        res = 0
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                left = i
                right = i+1
                while left >=0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1
                curRes = right - left - 1
                if curRes > res:
                    res = curRes
                    resLeft = left + 1
                    resRight = right - 1
        for i in range(len(s) - 2):
            if s[i] == s[i+2]:
                left = i
                right = i+2
                while left >=0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1
                curRes = right - left - 1
                if curRes > res:
                    res = curRes
                    resLeft = left + 1
                    resRight = right - 1
        return s[resLeft: resRight]
