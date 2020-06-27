class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        for i in range(len(s)):
            if s[i] != " ":
                break
        for j in range(len(s)-1,-1,-1):
            if s[j] != " ":
                break
        if i > j:
            return ""
        s = s[i:j+1]
        res = s.split(" ")
        '''
        注意split（） 如果不含参数的话就是将多个空格看成一个空格
        而split(" ")就只是分割一个空格
        '''
        res2 = []
        for s in res:
            if s!= "":
                res2.append(s)
        return " ".join(res2[::-1])

a = Solution()
s = "a good   example"
print(a.reverseWords(s))