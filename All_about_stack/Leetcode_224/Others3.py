'''
转化为逆波兰表达式的变体（方便写法
实际上是可以边转化边算不用加个queue再来算逆波兰，具体过程如下：

使用两个栈，stack0 用于存储操作数，stack1 用于存储操作符
从左往右扫描，遇到操作数入栈 stack0
遇到操作符时，如果当前优先级低于或等于栈顶操作符优先级，则从 stack0 弹出两个元素，从 stack1 弹出一个操作符，进行计算，将结果并压入stack0，继续与栈顶操作符的比较优先级。
如果遇到操作符高于栈顶操作符优先级，则直接入栈 stack1
遇到左括号，直接入栈 stack1。
遇到右括号，则从 stack0 弹出两个元素，从 stack1 弹出一个操作符进行计算，并将结果加入到 stack0 中，重复这步直到遇到左括号

作者：windliang
'''
class Solution:
    def calculate(self, s):
        if len(s) == 1:
            return int(s[0])
        def do_Plus_or_Sub(StackOp, stackNum):
            op = stackOp.pop()
            v1 = stackNum.pop()
            v2 = stackNum.pop()
            if op == '+':
                stackNum.append(v1 + v2)
            else:
                stackNum.append(v2 - v1)
        stackNum = []
        stackOp = []
        i = 0
        curNum = ''
        while i < len(s):
            if s[i].isdigit():
                while i<len(s) and s[i].isdigit():
                    curNum = curNum + s[i] #字符串拼接
                    i += 1
                stackNum.append(int(curNum))
                curNum = ''
            elif s[i] in '+-()':
                if s[i] == '(':
                    stackOp.append(s[i])
                elif s[i] in '+-':
                    if len(stackOp) > 0 and stackOp[-1] != '(' :
                        do_Plus_or_Sub(stackOp,stackNum)
                    stackOp.append(s[i])
                elif s[i] == ')':
                    while stackOp[-1]!= '(':
                        do_Plus_or_Sub(stackOp, stackNum)
                    stackOp.pop()
                i += 1
            else:
                i += 1
        while len(stackOp) > 0:
            do_Plus_or_Sub(stackOp, stackNum)
        return stackNum[-1]

if __name__ == '__main__':
    a = Solution()
    print(a.calculate("42"))


