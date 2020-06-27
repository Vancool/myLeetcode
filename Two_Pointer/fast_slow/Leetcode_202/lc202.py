class Solution(object):
    def isHappy(self, n):
        hashmap = set()
        def countBit(val):
            res = 0
            while val:
                key = val % 10
                res += key ** 2
                val = val // 10
            return res
        while n != 1 and n not in hashmap:
            hashmap.add(n)
            n = countBit(n)
        return n == 1





'''
这题我不会， 主要是找循环
因为递归下去数字不会无限增大而是会停留在[1:k] 的区间中
所以只要判断有没有出现之前遇到过的数字就好
这个利用的是 抽屉原理：

因为int类型最大值为为‭‭2 147 483 647‬‬， 所以平方和最大的数是1 999 999 999
1999999999 平方和为1 + 81*9 = 724。任何数的平方和都在1到724之间，724次循环之内一定有重复的

如何判断是否遇到过：
哈希表 or 循环中的快慢指针
用指针来表示下标脑海里模拟有个数组
'''

class Solution(object):
    def isHappy(self, n):
        def countBit(value):
            res = 0
            while value:
                key = value % 10
                res += key ** 2
                value = value // 10
            return res
        fast = n
        slow = n
        while True:
            slow = countBit(slow)
            fast = countBit(fast)
            fast = countBit(fast)
            if slow == fast or fast == 1:
                break
        return fast == 1
