class Solution(object):
    def removeKdigits(self, num, k):
        if k >= len(num): return "0"
        if k == 0: return num
        while k:
            subres = '9'*len(num)
            for i in range(len(num)):
                if num[0:i]+num[i+1::] < subres:
                    subres = num[0:i]+num[i+1::]
            k -= 1
            num = subres
        while num and num[0] == '0':
            num = num[1::]
        return num if num else "0"
'''
暴力解法， 超时
这题我不会
'''
a = Solution()
num = "10200"
k = 1
print(a.removeKdigits(num, k))
print("Done")