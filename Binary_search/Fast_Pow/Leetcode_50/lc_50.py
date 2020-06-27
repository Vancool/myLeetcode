class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 1 or x == 1:
            return x
        if n == 0:
            return 1
        is_negative = False
        if n < 0:
            is_negative = True
            n = -n
        stack = []
        k = n
        '''
        实际上我这一步求了反码，其实可以不用这样做的
        '''
        while k:
            if k&1:
                stack.append(1)
            else:
                stack.append(0)
            k = k >> 1
        stack.pop() #不要最后那个1
        base = x
        while stack:
            rem = stack.pop()
            x = x*x
            if rem:
                x = x*base
        if is_negative:
            return 1/x
        return x
