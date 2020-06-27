class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if len(str) == 0 or (not str[0].isdigit() and str[0] != '+' and str[0] != '-'):
            return 0
        is_negative = False
        res = 0
        if not str[0].isdigit():
            if str[0] == '-':
                is_negative = True
            if len(str) == 1 or not str[1].isdigit():
                return 0
            else:
               res += ord(str[1]) -ord('0')
            str = str[2:len(str)]
        for ch in str:
            if not ch.isdigit():
                break
            else:
                '''
                如果用java 用int来存数字，那么需要判断是否会溢出
                判断溢出的方法（正负）：
                if(res > INT_MAX / 10 ||(res == INT_MAX/10 and ch > 7)){
                    return flag > 0 ? INT_MAX : INT_MIN
                }
                '''
                res *= 10
                res += ord(ch) - ord('0')
        if is_negative:
            return -res if res <= 2**31 else -2**31
        return res if res < 2**31 else 2**31 - 1
'''
ord() 字符转ascii
chr() ascii转字符
'''



a = Solution()
s = "words and 987"
print(a.myAtoi(s))
print("Done")