class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 1:
            return int(s[0])
        backQueue =[] #逆波兰表达式存储的队列
        opStack =[] #存储运算符的栈
        processStack =[]
        i = 0
        key =''
        '''获得逆波兰表达式'''
        while(i < len(s)):

            if s[i] == ' ':
                i += 1
                continue
            if s[i] == '(':
                opStack.append(s[i])
                i += 1
                continue
            elif s[i] in '+-':
                if  len(opStack)== 0:
                    opStack.append(s[i])
                elif opStack[-1] == '(':
                    opStack.append(s[i])
                else:
                    backQueue.append(opStack.pop())
                    opStack.append(s[i])
                i += 1
                continue
            elif s[i] == ')':
                while opStack[-1] != '(':
                    backQueue.append(opStack.pop())
                opStack.pop() #把（也pop掉
                i+= 1
                continue
            while i<len(s) and s[i].isdigit():
                key = key + s[i]
                i += 1
            backQueue.append(int(key))
            key = ''
        if len(opStack)!= 0:
            key = opStack.pop()
            if key in '-+':
                backQueue.append(key)
        '''计算逆波兰表达式'''
        for key in backQueue:

            if key == '+':
                v2 = processStack.pop()
                v1 = processStack.pop()
                processStack.append(v2+v1)
            elif key == '-':
                v2 = processStack.pop()
                v1 = processStack.pop()
                processStack.append(v1-v2)
            else:
                processStack.append(key)
        return processStack[-1]
if __name__ == "__main__":
    a = Solution()
    k = input()
    print(a.calculate(k))



