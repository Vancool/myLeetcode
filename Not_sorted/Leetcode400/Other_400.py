class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        limit = 9
        digit = 1
        while n > digit * limit:
            n -= digit * limit
            limit *= 10
            digit += 1
        n -= 1
        '''
        这一步很重要，不写只会很麻烦
        因为如果是 n = 190 两位之前就是189个
        然后 此时 n = 190-189 = 1 digit = 3 
        n % digit  = 1 的确是找三位数的第一个
        
        但是 n = 192  n = 192-189 = 3
        n % digit = 0 就变成了要转换成第三个了
         
         同时找n的真实值也很麻烦，因为要用ceil来取
         而n-1就巧妙地将位数变为从0开始最后一位也不会进位了
        '''
        val, mod = divmod(n, digit)
        value = 10**(digit-1) + val
        return int(str(value)[mod])
