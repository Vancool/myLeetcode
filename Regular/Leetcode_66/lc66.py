class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            digits[i] = 0

        return digits.insert(0, 1)
        #return [1]+digits
'''
两种策略：
1. 转成数字+1再转回字符串
2. 直接加按位处理
'''

a = Solution()
k = [1,2,9]
print(a.plusOne(k))