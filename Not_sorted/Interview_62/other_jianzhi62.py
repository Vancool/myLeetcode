class Solution(object):
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if n == 1 or m == 1:
            return list(range(n))[-1]
        index = 0
        for i in range(2,n+1):
            index = (index + m) % i
        return index

'''
约瑟夫环问题
我是看这个人的解析学会的
https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/huan-ge-jiao-du-ju-li-jie-jue-yue-se-fu-huan-by-as/
'''

'''
也可以用递归来做，但是其实公式是一样的，是按这个人的公式来写的
https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/chi-jing-stsu-degd-degtsu-tu-jie-yue-se-fu-huan-hu/
但是如果写成循环其实还是一样的
'''

class Solution(object):
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if n == 1:
            return 0
        index = 0
        for i in range(2, n+1):
            index = (int(m%i) + index) % i
        return index