from collections import deque
'''
想到了用栈，但是不会处理
但是其实不是用栈，因为这个涉及到两边的不单调的数量，所以要统计两边的数量而不是一碰到就弹出的概念
我自己的解法写错了

'''
class Solution(object):
    def candy(self, ratings):
        if len(ratings) == 0:
            return 0
        maxInt = 1<<31 - 1
        ratings.append(maxInt)
        stack = deque()
        res = 0
        canndycount = 1
        stack.append(ratings[0])
        for i in range(1, len(ratings)):
            if len(stack) > 0 and stack[-1] < ratings[i]:
                while len(stack) > 0:
                    cur = stack.popleft()
                    res += canndycount
                    while len(stack) > 0 and cur ==  stack[-1]:
                        res += canndycount
                        cur = stack.pop()
                    if len(stack) > 0:
                        canndycount -= 1
                canndycount += 1
            elif len(stack) > 0 and stack[-1] == ratings[i]:
                while len(stack) > 0:
                    cur = stack.popleft()
                    res += canndycount
                    while len(stack) > 0 and cur ==  stack[-1]:
                        res += canndycount
                        cur = stack.pop()
                    if len(stack) > 0:
                        canndycount -= 1
                canndycount = 1
            else:
                canndycount += 1
            stack.append(ratings[i])
        return res
'''
test case:
[1,3,2,2,1]
'''


a = Solution()
r = [2]
print(a.candy(r))
print("Done")