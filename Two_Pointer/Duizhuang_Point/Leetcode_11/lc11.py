class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        tmpH = -1
        res = 0
        while left < right:
            if height[left] <= height[right]:
                if height[left] > tmpH:
                    tmpH = height[left]
                    res = max(tmpH*(right-left), res)
                left += 1
            else:
                if height[right] > tmpH:
                    tmpH = height[right]
                    res = max(tmpH*(right-left), res)
                right-= 1
        return res

'''
当存在两个变量，一个变小一个变大可以考虑用双指针，然后从最方便最大的地方开始对撞持续缩小
这样的话只需要考虑另一个变量会不会变大，求出另一个变大的变量是否造成结果改变就好
对撞双指针就是考虑如何固定一个移动另一个改变结果
但是其实是把迭代剪枝先求出极大值然后与别的极大值做对比 长度为n范围内的极大值

这一题的好一点在于是求小的值和下标差的乘积， 可以固定住一个往左或者右走
如果是求大的值和下标差乘积就要求两边到下标的距离了
'''