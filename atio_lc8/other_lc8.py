class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip()
        res = 0
        sign = 1
        index = 0
        MAX_INT = 1 << 31
        if len(str) == 0:
            return 0
        if str[0] == '-':
            sign = -1
        if not str[0].isdigit() and (str[0] == '+' or str[0]== '-'):
            index += 1
        for i in range(index, len(str)):
            if not str[i].isdigit():
                break
            else:
                if res > MAX_INT//10 or (res == MAX_INT//10 and str[i]> '7'):
                    return sign*MAX_INT if sign == -1 else MAX_INT-1
                res *= 10
                res += ord(str[i]) - ord('0')
        return sign * res
'''
自己已经写出来了
但是这样处理会更加简洁一些
直接做 1<<31 会比 2**31快
注意处理越界
 if res > MAX_INT//10 or (res == MAX_INT//10 and str[i]> '7'):
'''