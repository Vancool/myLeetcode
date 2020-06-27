'''
很巧妙地用栈来压入之前已经算过的
用sign 来表明下一个是加正数还是负数

'''
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = ''
        sign = 1
        res = 0
        i = 0
        while(i<len(s)):
            if s[i].isdigit():
                while i<len(s) and s[i].isdigit():
                    operand = operand + s[i]
                    i += 1
                res += sign*int(operand)
            if i == len(s):
                break
            else:
                operand = ''
                if s[i] == '+':
                    sign = 1
                elif s[i] == '-':
                    sign = -1
                elif s[i] =='(':
                    stack.append(res)
                    stack.append(sign)
                    res = 0
                    sign = 1
                elif s[i] ==')':
                    sign = stack.pop()
                    res = stack.pop()+sign*res
                    sign = 1

                i += 1
        return res

if __name__ == "__main__":
    a = Solution()
    print(a.calculate("(1-(4+5+2)-3)+(6+8)"))




