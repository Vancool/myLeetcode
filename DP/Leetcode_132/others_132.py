class Solution(object):
    def minCut(self, s):
        if len(s) <= 1: return 0
        dp = [[False] * len(s) for _ in range(len(s))]
        min_cut_count = [float('inf')] * len(s)
        for right in range(len(s)):
            for left in range(right+1):
                dp[left][right] = s[left] == s[right] and ((right - left) <= 2 or dp[left+1][right-1])
            if dp[0][right]: min_cut_count[right] = 0
            else:
                for i in range(1,right+1):
                    if dp[i][right]:
                        min_cut_count[right] = min(min_cut_count[right], min_cut_count[i-1]+1)
        return min_cut_count[-1]

'''
其实记录切割大小也是会重复的
比如试试画 aababc的切割

另一种写法：
'''
class Solution(object):
    def minCut(self, s):
        if len(s) <= 1: return 0
        dp = [[False] * len(s) for _ in range(len(s))]
        min_cut_count = [float('inf')] * len(s)
        for right in range(len(s)):
            for left in range(right+1):
                dp[left][right] = s[left] == s[right] and ((right - left) <= 2 or dp[left+1][right-1])
                if dp[left][right]:
                    if left == 0:
                        min_cut_count[right] = 0
                    else:
                        min_cut_count[right] = min(min_cut_count[right], min_cut_count[left-1] + 1)


        return min_cut_count[-1]


'''
另一种DP: 使用中心扩散的方法决定由某个字符往两边扩散，记录回文子串最右边最小的分割次数
'''
class Solution(object):
    def minCut(self, s):
        if len(s) <= 1: return 0
        dp = [i for i in range(len(s))]
        for i in range(1, len(s)):
            # 奇数
            dp[i] = min(dp[i], dp[i-1] + 1)
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                dp[right] = min(dp[right], dp[left-1] + 1) if left-1 >= 0 else 0
                left -= 1
                right += 1
            # 偶数
            left = i-1
            right = i
            while left >= 0 and right <len(s) and s[left] == s[right]:
                dp[right] = min(dp[right], dp[left-1] + 1) if left -1 >= 0 else 0
                left -= 1
                right += 1
        return dp[-1]


'''
这个中心扩散的代码写得可真是优雅
'''
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            return 0
        for i in range(1,len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        cut = [x for x in range(-1, len(s))]
        for i in range(len(s)):
            r1, r2 = 0, 0
            while i-r1 >= 0 and i+r1 < len(s) and s[i-r1] == s[i+r1]:
                cut[i+r1+1] = min(cut[i+r1+1],cut[i-r1]+1)
                r1 += 1
            while i-r2 >= 0 and i+ r2 +1 < len(s) and s[i-r2] == s[i+r2+1]:
                cut[i+r2+2] = min(cut[i+r2+2], cut[i-r2]+1)
                r2 += 1
        return cut[-1]
a =Solution()
print(a.minCut('efe'))