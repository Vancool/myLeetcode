from collections import deque
'''
https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/
滑动窗口思想：
本来是每个都要从头开始遍历的，但是不这样做了
用两个指针一个指着左边一个指着右边，这样只要加右边减去左边就好
因为走过的数是要被加上的，那么就不会因为滑动错过答案
'''
class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        left = 1
        right = 0
        res = []
        subres = deque()
        val = 0
        while left < right or right == 0:
            while val < target:
                right += 1
                val += right
                subres.append(right)
            if val == target:
                res.append(list(subres))
                val -= subres.popleft()
                left += 1
            elif val > target:
                val -= subres.popleft()
                left += 1
        return res

'''
可以不用滑动窗口，因为直接是等差数列，因此可以等差数列求和
x - x+i的和
(x + x+i)*(i+1)/ 2 = target
然后用间隔i计算 x 
数学的方法
'''

class Solution1(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        i = 1
        res = []
        while target >= (3*i+2+i*i)/2:
            if not (target - i*(i+1)//2) %(1+i):
                x = int((target - i*(i+1)//2)//(i+1))
                res.append(list(range(x, x+i+1)))
            i += 1
        return res[::-1]

a = Solution1()
print(a.findContinuousSequence(9))
print("Done")


