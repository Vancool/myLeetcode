class Solution(object):
    def convertToTitle(self, n):
        res = ""
        while n > 0:
            n -= 1
            key = int(n % 26)
            res = chr(key + ord('A')) + res
            n = n // 26
        return res


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        base = 26
        strs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = []
        while n:
            n -= 1
            ans.append(strs[n % base])
            n = n / base
        return "".join(ans[::-1])


class Solution(object):
    def convertToTitle(self, n):
        res = ""
        while n:
            n, y = divmod(n, 26)
            if y == 0:
                n -= 1
                y = 26
            res = chr(y + 64) + res
        return res

a = Solution()
print(a.convertToTitle(701))
