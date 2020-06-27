class Solution(object):
    def decodeString(self, s):
        if len(s) == 3: return s[1]
        stack = []
        i = 0
        s = '[' + s + ']'
        while i < len(s):
            if s[i] == '[':
                if not stack or not stack[-1].isdigit():
                    stack.append('1')
                i += 1
                continue
            elif s[i] == ']':
                str = ""
                while stack and not stack[-1].isdigit():
                    str = stack.pop() + str
                time = stack.pop()
                ch = str * int(time)
                i += 1
                stack.append(ch)
            elif s[i].isdigit():
                end = i
                while end < len(s) and s[end].isdigit():
                    end += 1
                ch = s[i: end]
                i = end
                stack.append(ch)
            else:
                end = i
                while end < len(s) and not s[end].isdigit() and s[end]!= ']' and s[end] != '[':
                    end += 1
                ch = s[i: end]
                i = end
                stack.append(ch)

        return stack[-1]
'''
自己写得还是比较乱
用栈 或者 递归
'''
class Solution(object):
    def decodeString(self, s):
        if len(s) == 3: return s[1]
        self.index = 0
        def process():
            res = ""
            number = 0
            while self.index < len(s):
                if '0' <= s[self.index] <= '9':
                    number = number * 10 + int(s[self.index])
                    self.index += 1
                elif s[self.index] == '[':
                    self.index += 1
                    res = res + number * process()
                    number  = 0
                elif s[self.index] == ']':
                    self.index += 1
                    return res
                else:
                    res += s[self.index]
                    self.index += 1
            return res
        return process()
a = Solution()
s = "3[a]2[bc]"
print(a.decodeString(s))



