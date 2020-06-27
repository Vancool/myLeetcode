class Solution(object):
    def majorityElement(self, nums, m = 2):
        if len(nums) == 0: return []
        if len(nums) == 1: return nums
        cand = [0] * m
        count = [0] * m
        for n in nums:
            i = 0
            while i < m:
                if cand[i] == n:
                    count[i] += 1
                    break
                # 判断是否相同一定要提前写， 否则会填上相同的数导致重复
                i += 1
            if i >= m:
                i = 0
                while i < m:
                    if count[i] == 0:
                        count[i] += 1
                        cand[i] = n
                        break
                    i += 1
            if i >= m:
                for i in range(m):
                    count[i] -= 1
        res = []
        for i in range(m):
            if count[i] > 0:
                tmp = 0
                for n in nums:
                    if n == cand[i]:
                        tmp += 1
                if tmp > len(nums) // (m+1):
                    res.append(cand[i])
        return res
a = Solution()
nums = [-1,1,1,1,2,1]
print(a.majorityElement(nums))
'''
这题我不会，摩尔投票法
'''