class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 1:
            return int(s[0])
        def countOp(numStack, opStack):
            op = opStack.pop()
            v1 = numStack.pop()
            v2 = numStack.pop()
            if op == '+':
                numStack.append(v1+v2)
            elif op == '-':
                numStack.append(v2-v1)
            elif op == '*':
                numStack.append(v2*v1)
            elif op == '/':
                numStack.append(int(v2/v1))
        stackOp =[]
        stackNum = []
        ten_base = 0
        i = 0
        curNum = 0
        while i<len(s):
            if s[i].isdigit():
                while i<len(s) and s[i].isdigit():
                    curNum = 10*curNum+int(s[i])
                    ten_base += 1
                    i += 1
                stackNum.append(curNum)
                curNum = 0
                ten_base = 0
            elif s[i] in '+-*/':
                if len(stackOp)==0 :
                    stackOp.append(s[i])
                elif s[i] in '+-':
                    while len(stackOp)>0:
                       countOp(stackNum,stackOp)
                    stackOp.append(s[i])
                elif s[i] in '*/':
                    if stackOp[-1] in '*/':
                        countOp(stackNum,stackOp)
                    stackOp.append(s[i])
                i += 1
            else:
                i += 1
        while len(stackOp)>0:
            countOp(stackNum,stackOp)
        return stackNum[-1]

if __name__ == '__main__':
    a =Solution()
    print(a.calculate("1337"))


