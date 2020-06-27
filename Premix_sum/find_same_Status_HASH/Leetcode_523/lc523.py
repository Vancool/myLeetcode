class Solution(object):
    def checkSubarraySum(self, nums, k):
        if len(nums) < 2: return False
        for i in range(len(nums)-1):
            res = nums[i]
            for j in range(i+1,len(nums)):
                res += nums[j]
                if res == k or (k != 0 and res % k):
                    return True
        return False
'''
这题要注意 k == 0 的情况
'''
'''
原来可以用 前缀和 + 状态 来考虑这题！！
因为如果是求是否整除的话只需要判断前缀和余数是否相等就好！！
另外这题是至少有两个元素，
前缀和最好加一个(0,-1) 的没有元素的初始位置， 
判断的时候要判断是否数组里面是否有多于两个元素，因此不能用set()
'''

class Solution(object):
    def checkSubarraySum(self, nums, k):
        if len(nums) < 2: return False
        '''
        if k != 0 and k <= len(nums): return True
        不能用抽屉原理加这个判断，因为如果哈希值相同相邻放一起也是合理的
        '''

        hashmap = {}
        val = 0
        hashmap[0] = -1
        for i in range(len(nums)):
            val += nums[i]
            key = val
            if k != 0:
                key %= k
            if key in hashmap:
                if i - hashmap[key] >= 2:
                    return True
            else:
                hashmap[key] = i
        return False


a = Solution()
nums = [7,0,0,0,0]
print(a.checkSubarraySum(nums, 0))