class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4:
            return []
        if len(s) == 4:
            return ['.'.join(s)]
        res = []

        def Process(pre, start, depth, s):
            if start >= len(s):
                return
            if depth == 3:
                if start >= len(s) or int(s[start:len(s)]) > 255:
                    return
                else:
                    if s[start] == '0' and len(s) - start > 1:
                        return
                    res.append(pre + '.' + s[start:len(s)])
                    return
            if depth > 0:
                pre = pre + '.'
            for i in range(3):
                if s[start] == '0':
                    Process(pre+s[start], start+1, depth+1, s)
                    break
                if i == 2 and int(s[start: start + 3]) > 255:
                    break
                Process(pre + s[start: start + i + 1], start + i + 1, depth + 1, s)

        Process('', 0, 0, s)
        return res
'''
test case:
1.
"010010"
如果是字符串和int的转换处理问题，一定要注意开头是0的状况

2.
"11111"
不仅仅是在第三层会出现越界，要在每一层访问的时候考虑越界问题
'''
a = Solution()
s = "010010"
print(a.restoreIpAddresses(s))
print("Done")
