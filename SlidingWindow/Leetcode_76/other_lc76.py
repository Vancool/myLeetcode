
class Solution(object):
    def minWindow(self, s, t):
        if len(s) < len(t): return ""
        Tdic = {}
        for ch in t:
            Tdic[ch] = Tdic.get(ch,0) + 1
        left = 0
        right = 0
        minleft = 0
        min_dis = len(s) + 1
        count = 0
        while right < len(s):
            if s[right] in Tdic:
                Tdic[s[right]] -= 1
                if Tdic[s[right]] >= 0:
                    count += 1
            if count == len(t):
                while s[left] not in Tdic or Tdic[s[left]] < 0:
                    if s[left] in Tdic and Tdic[s[left]] < 0: Tdic[s[left]] += 1
                    left += 1
                if right - left + 1 < min_dis:
                    min_dis = right - left + 1
                    minleft = left
                Tdic[s[left]] += 1
                count -= 1
                left += 1
            right += 1
        return s[minleft: minleft+min_dis] if min_dis <= len(s) else ""

a = Solution()
S = "ADOBECODEBANC"
T = "C"
print(a.minWindow(S, T))