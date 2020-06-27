class Solution(object):
    def twoSum(self, numbers, target):
        if len(numbers) <2:
            return []
        left = 0
        right = len(numbers) - 1
        while left < right:
            cur = numbers[left] + numbers[right]
            if cur == target:
                return [left+1, right+1]
            if cur > target:
                right -= 1
            else:
                left += 1
        return []

'''
对撞双指针的另一个使用位置：
排序好的数组，求和，可以根据大小决定固定哪个往哪里移动
忽然想起好像有一题是在矩阵图里然后往哪里移动可以找到数的，也可以大小来决定往哪个方向移动
'''