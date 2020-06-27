'''
直接用倒序来解决括号用栈和运算用队列的尴尬
'''
class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 1:
            return int(s[0])
        stack = []
        res = 0
        n = 0
        curNum = 0
        op = 1
        for i in range(len(s)-1,-1,-1):
            if s[i].isdigit():
                curNum += 10**n*int(s[i])
                n += 1
            elif s[i] in '()+-':
                if n>0:
                    stack.append(curNum)
                    curNum = 0
                    n = 0
                if s[i] == '(':
                    '''此处弹出（）里面的东西加上运算'''
                    while stack[-1]!=')':
                        key = stack.pop()
                        if key == '+':
                            op = 1
                        elif key == '-':
                            op = -1
                        else:
                            res += op*key
                            op = 1
                    stack.pop() #pop '('
                    stack.append(res)
                    res = 0
                else:
                    stack.append(s[i])
        if n!= 0: #这个地方还是用while循环会方便很多，这样就不需要考虑最后一个字符是数字的情况
            stack.append(curNum)
        while len(stack) > 0:
            key = stack.pop()
            if key == '+':
                op = 1
            elif key == '-':
                op = -1
            else:
                res += op* key
        return res

if __name__ == '__main__':
    a = Solution()
    print(a.calculate("1+1"))