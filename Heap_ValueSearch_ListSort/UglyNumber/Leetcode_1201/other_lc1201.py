class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        def get_smallest_common(a,b):
            ab = a*b
            while a%b != 0 and a%b != b:
                a, b = b, a%b
            return int(ab//int(b))

        def count_num(val, a, b, c, ab, ac, bc, abc):
            return val//a + val//b + val//c - val//(ab) - val//(bc) - val//(ac) + val//abc
        left = min(a,b,c)
        ab = get_smallest_common(a,b)
        ac = get_smallest_common(a,c)
        bc = get_smallest_common(b,c)
        abc = get_smallest_common(ab, c)
        right = n * left
        mid = left + (right - left) // 2
        while left <= right:
            mid = left + (right - left)//2
            num = count_num(mid, a, b, c, ab, ac, bc, abc)
            if num > n:
                right = mid-1
            elif num < n:
                left = mid+1
            else:
                break
        return (mid - int(min(mid % a, mid % b, mid % c)))

s = Solution()
n = 5
a = 2
b = 11
c = 13
print(s.nthUglyNumber(n,a,b,c))