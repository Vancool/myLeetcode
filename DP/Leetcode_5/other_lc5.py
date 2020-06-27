class Solution1(object):
    def longestPalindrome(self, s):
        if len(s) == 0 or len(s) == 1:
            return s
        dp = [[False] * len(s) for _ in range(len(s))]
        maxStart = -1
        maxLen = 0
        for i in range(len(s)-1,-1,-1):
            for j in range(i, len(s)):
                if s[i] == s[j] and ((j-i+1) <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if (j-i+1) > maxLen:
                        maxLen = j-i+1
                        maxStart = i
        return s[maxStart: maxStart+maxLen]
'''
https://leetcode-cn.com/problems/longest-palindromic-substring/submissions/
我自己是用中心扩散做的
官方给出了dp的做法：
  暴力枚举求解 s[i:j] 字串是不是回文子串 ---> 发现很多重复 
  ---> dp(i,j) = 判断第i和第j个字符相等且 s(i+1,j-1）也是字串
  复杂度也是 O（n^2）
  
空间优化比较复杂
可以先看这个图看看算法是怎么走的
https://pic.leetcode-cn.com/d6f6d0af1b55319252b81dc409848103da69bb043a9a13e8d6878574ac10e5cf-image.png
如何简化成一个数组呢
我们可以第 i 轮用 i+1 轮的数组,只用一个数组存上一轮的东西
j从后往前遍历， 因为推导方向是这样的 （i+1,j-1） --> (i, j)  i+1的数组的j-1格并没有被覆盖掉，可以直接用
'''
class Solution(object):
    def longestPalindrome(self, s):
        if len(s) == 0 or len(s) == 1:
            return s
        dp = [False] * len(s)
        maxStart = -1
        maxLen = 0
        for i in range(len(s)-1,-1,-1):
            for j in range(len(s)-1,i-1, -1):
                if s[i] == s[j] and ( (j-i+1) <= 2 or dp[j-1]):
                    dp[j] = True
                    if j-i+1 > maxLen:
                        maxStart = i
                        maxLen = j - i + 1
                else:
                    dp[j] = False
        return s[maxStart:maxStart + maxLen]
a = Solution()
print(a.longestPalindrome("abcda"))
print("Done")