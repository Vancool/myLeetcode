from collections import deque
class Solution(object):
    def removeKdigits(self, num, k):
        if k >= len(num): return "0"
        stack = deque()
        for key in num:
            while stack and k and stack[-1] > key:
                stack.pop()
                k -= 1
            stack.append(key)

        while k > 0:
            stack.pop()
            k -= 1
        while stack and stack[0] == '0':
            stack.popleft()
        '''
        官方直接用了切片的写法，非常优雅
        finalStack = numStack[:-k] if k else numStack
        '''
        return "".join(stack) if stack else "0"

'''
这题我不会，没找到删除的策略
其实如果删除一位数， 找删除数的时候看看它和左右两边数字大小的关系来定删除策略
像这题就是从左往右删， 如果右边有数那么删左边大的， 如果右边没有数了就从末尾往前删
看两两或者三三的组合来考虑删除策略。

其实这题也可以看是找逆序对消除最左边的逆序对的最大值 或者是消除偏向右边的正序对的最大值
'''
a = Solution()
num = "10200"
k = 1
print(a.removeKdigits(num, k))

