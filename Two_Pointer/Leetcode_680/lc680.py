class Solution(object):
    def validPalindrome(self, s):

        def Process(left, right):
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        if len(s) <= 2:
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                #print(s[left], s[right])
            else:
                return Process(left+1, right) or Process(left, right - 1)
        return True
'''
还是要用递归
不能在单纯在循环中判断选择走 左边的下一个和右边 还是 右边的下一个和左边 ， 其中一个还是可能会走通的
如果用 if-else 判断就会截断
test case:
"aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
'''
a = Solution()
s = "abca"
print(a.validPalindrome(s))
print("Done")
