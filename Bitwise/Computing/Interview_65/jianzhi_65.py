class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        plusOne = 0
        res = 0
        for i in range(32):
            mask = 1<<i
            key = (plusOne<<1) ^ (a&mask)^(b&mask)
            plusOne = (plusOne and (a&mask)) or (plusOne and (b&mask)) or ((a&mask) and (b&mask))
            res = res | key
        return res if res < 0x80000000 else ~(res ^ 0xFFFFFFFF)

k = Solution()
a = 1
b = -2
print(k.add(a,b))
print("Done")