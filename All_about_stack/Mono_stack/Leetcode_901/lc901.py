from collections import deque
class StockSpanner(object):
    def __init__(self):
        self.stack = deque()
    def next(self, price):
        res = 1
        while self.stack and price >= self.stack[-1][0]:
            count = self.stack.pop()[1]
            res += count
        self.stack.append((price, res))
        return res

