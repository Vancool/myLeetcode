class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        key = 1
        res = 0
        for i in range(32):
            count = 0
            for n in nums:
                count += n & key
            if int(count%3):
                res |= key
            key = key<<1
        return res-2**32 if res > 2**31-1 else res
'''
这个是按每个位 int 4字节 32位来看
注意后面如果是负数的话数字会超过 2**31
因此要减去 2**32来计算负数
'''
