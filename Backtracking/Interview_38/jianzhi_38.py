class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) == 0:
            return []
        if len(s) == 1:
            return [s]
        res = []
        def Process(head, s, res):
            if len(s) == 1:
                res.append(head+s)
                return
            has_key = set()
            for i in range(len(s)):
                if s[i] in has_key:
                    continue
                else:
                    has_key.add(s[i])
                    Process(head+s[i],s[0:i] + s[i+1:len(s)], res)
        Process("", s, res)
        return res

a = Solution()
s = "aba"
print(a.permutation(s))
print("Done")


