class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 2:
            return nums
        '''
        位运算，多么性感的操作。
        异或的基本知识: 相同为0，不同为1，异或本身为0，异或0为本身
        a^a=0
        a^0=a
        a^b^c=a^c^b 符合交换律和结合律
        负数在计算机以补码形式存在
        a&(-a)=最低位为1的二进制（就是最右边的1
        最容易看懂的解析是这个：
        https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/solution/c-0ms-chao-ji-xiang-xi-jie-shi-kan-bu-dong-de-ji-2/
        '''
        count = 0
        for n in nums:
            count = count ^ n
        key = count & (-count)
        stack1 = []
        for n in nums:
            if n & key:
                stack1.append(n)
        res = []
        val = 0
        for n in stack1:
            val = val ^ n
        res.append(val)
        res.append(val ^ count)
        return res


print(0 ^ 0)

