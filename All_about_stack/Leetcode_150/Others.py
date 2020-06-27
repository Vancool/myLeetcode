class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        if len(tokens) == 2:
            if tokens[0] == '-':
                return -int(tokens[1])
            else:
                return int(tokens[1])
        stack = []
        res = 1
        if tokens[0] == "-":
            res = -1
            tokens = tokens[1:len(tokens)]
        if tokens[0] == "+":
            tokens = tokens[1:len(tokens)]
        for val in tokens:
            if val not in '+-*/':
                stack.append(int(val))
            else:
                v2 = stack.pop()
                v1 = stack.pop()
                if val == '+':
                    stack.append(v2+v1)
                elif val == '*':
                    stack.append(v2*v1)
                elif val == '-':
                    stack.append(v1-v2)
                elif val == '/':
                    stack.append(int(v1/v2))
                    '''
                    python3 负数 //运算向下取整
                    所以先转化为小数/ 然后再int()截取整数部分
                    或者是先全部转成正数运算最后转成负数[python2方法，因为python2 /没办法得到截取前的小数]
                 '''
        return stack[0]*res
if __name__ == "__main__":
    a = Solution()
    print(a.evalRPN( ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))