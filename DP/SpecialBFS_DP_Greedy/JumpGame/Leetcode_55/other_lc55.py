from collections import deque
class Solution1(object):
    def canJump(self, nums):
        if len(nums) == 1:
            return True
        if len(nums) == 0 or nums[0] == 0:
            return False
        maxVisit = 0
        for i in range(len(nums)):
            if i <= maxVisit:
                maxVisit = max(maxVisit, nums[i] + i)
                if maxVisit >= len(nums) - 1:
                    return True
            else:
                return False
'''
跳跃游戏
https://leetcode-cn.com/problems/jump-game/
这个是用贪心来做
实际上是个隐式加速的BFS， 只不过一维数组的BFS可以优化成为greedy
因为它是遍历走过的路，然后每次更新最远可达的路
只是遍历的方式是先深度搜索搜到最深的地方，然后发现走不通就往回走看回去的路走不走得通
贪心算法只是先标记一个最大能走通的，然后从近往远走

下面是BFS的写法：
'''
class Solution2(object):
    def canJump(self, nums):
        if len(nums) == 1:
            return True
        if len(nums) == 0:
            return False
        q = deque()
        visited = set()
        visited.add(0)
        q.append(0)
        while q:
            idx = q.pop()
            if idx >= len(nums)-1 or nums[idx] + idx >= len(nums) - 1:
                return True
            if idx >= 0 and nums[idx] == 0 or idx+nums[idx] in visited:
                idx -= 1
                while idx in visited:
                    idx -= 1
                    continue
                if idx == -1:return False
                else:
                    q.append(idx)
                    visited.add(idx)
            else:
                q.append(idx + nums[idx])
                visited.add(idx + nums[idx])
        return False

'''
我自己也是用
另一种DP的想法： 
dp[i] 表示能够走到的最大的位置,直接转换题目思路不是是否能走到而是走到哪里做个判断
dp[i] 指从0走到i后的下一个最大能走到的下标（前i个元素能到达的最远位置
这样就和greedy是一样的了
'''
class Solution2(object):
    def canJump(self, nums):
        if len(nums) == 1:
            return True
        if len(nums) == 0:
            return False
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            if i > dp[i-1]:
                return False #第i个走不到
            else:
                dp[i] = max(dp[i-1], i + nums[i])
                if dp[i] >= len(nums) - 1:
                    return True
        return False
'''
这边的dp可以优化，优化之后就是greedy了
'''

a = Solution2()
nums = [3,0,8,2,0,0,1]
print(a.canJump(nums))







