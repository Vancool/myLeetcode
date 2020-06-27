class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xFFFFFFFF
        '''
        注意： a 和 b与 mask &是不可以省的，因为如果a 或者b是负数， 那么32位之前的位（33.34位）都是1
        这样如果取 ^ 就会出错
        
        正数/负数 加减法都可以用加法代替 补码也是可以加法的，别想太多
        不带进位加法 a ^ b
        算当前位是否进位： a & b 
        处理res为负数的情况： ~(res ^ 0xFFFFFFFF) 这样是先异或把前面的1全部转化成0之后取反
                                                就能够把32位之前的1全部补上，不然会溢出
        
        '''
        a &= mask
        b &= mask
        res = a
        while b:
            carry = res & b
            res ^= b
            b = (carry << 1) & mask
        return res if res < 0x80000000 else ~(res ^ 0xFFFFFFFF)

a =Solution()
print(a.getSum(-1,1))
print(0x80000000)
print("Done")