class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s =s.strip()
        if len(s) == 0:
            return ""
        res = []
        left =  right = len(s)-1
        while left >= 0:
            while left >= 0 and s[left] != " ":
                left -= 1
            res.append(s[left+1: right+1])
            while left >= 0 and s[left] == " ":
                left -= 1
            right = left
        return " ".join(res)

a = Solution()
s = "a"
print(a.reverseWords(s))
