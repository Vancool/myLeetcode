class Solution(object):
    def validPalindrome(self, s):
        def equal_str(s):
            left = 0
            right = len(s)-1
            while left < right and s[left] == s[right]:
                left += 1
                right -= 1
            return right <= left
        if len(s) == 0 or len(s) == 1:
            return True
        left = 0
        right = len(s)-1
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        if left < right:
            return equal_str(s[left+1: right+1]) or equal_str(s[left:right])
        return True