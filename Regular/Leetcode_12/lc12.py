class Solution(object):
    def intToRoman(self, num):
        key = ['I','V','X','L','C','D','M']
        res = ""
        base = 0
        while num:
            value = num % 10
            if value == 4:
                res = key[base] + key[base+1] + res
            elif value == 9:
                res = key[base] + key[base+2] + res
            elif value == 5:
                res = key[base+1] + res
            elif value < 5:
                res = key[base] * value + res
            else:
                res = key[base+1] + key[base] *(value - 5) + res
            base += 2
            num //= 10
        return res

'''
另一种做法： 贪心
但是我还是比较喜欢我的写法，比较好解释
'''
class Solution(object):
    def intToRoman(self, num):
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = ""
        index = 0
        while num:
            while num >= nums[index]:
                num -= nums[index]
                res += romans[index]
            index += 1
        return res
