import math
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        limit = 0
        ceil = 9
        val = 0
        count = 1
        res = 0
        while n > limit or limit == 0:
            if n > ceil:
                val += (ceil-limit)//count
                limit = ceil
                count += 1
                ceil += count * (10**count-1 - val)

            else:
                val += math.ceil((n-limit)/count) #是哪个数
                key = int((n-limit-1)%count)+1 #第几位
                count -= 1
                res = val
                while key:
                    res = val //(10**count)
                    val = val - res*(10**count)
                    count -= 1
                    key -= 1
                break
        return res

a = Solution()
print(a.findNthDigit(10))
print("Done")
