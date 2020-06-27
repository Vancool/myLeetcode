'''
包括括号的计算器解法
其中对栈处理乘除非常elegant

'''
'''
我觉得这题最elegant的写法
'''
class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        stack = list()
        op = '+'
        for i, c in enumerate(s):
            if c.isnumeric():
                num = num*10+int(c)
            if c in '+-*/' or i == len(s)-1:
                if op == '+':
                    stack.append(num)
                if op == '-':
                    stack.append(-num)
                if op == '*':
                    stack.append(stack.pop()*num)
                if op == '/':
                    stack.append(int(stack.pop()/num))
                op = c
                num = 0
        return sum(stack)

'''
带括号方法
'''
class Solution1(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def helper(s,index):
            stack =[]
            sign ='+'
            num = 0
            while index<len(s):
                if s[index].isdigit():
                    num = 10*num + int(s[index])
                    index += 1
                if index>=len(s) and num!= 0:
                    if sign == "+":
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack.append(stack.pop()*num)
                    elif sign == '/':
                        stack.append(int(stack.pop()/ float(num)))
                elif index<len(s) and s[index]!=' ':
                    if s[index] == "(":
                        index,num = helper(s, index+1)
                    if sign == "+":
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack.append(stack.pop()*num)
                    elif sign == '/':
                        stack.append(int(stack.pop()/ float(num)))
                    elif sign == ")":
                        return index,sum(stack)
                    num = 0
                    sign = s[index]
                    index += 1
            return index,sum(stack)
        res = helper(s,0)[1]
        return res

if __name__ == "__main__":
    a = Solution()
    print(a.calculate('3-5/2'))