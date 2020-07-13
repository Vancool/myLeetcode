from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        n1 = Counter(nums1)
        n2 = Counter(nums2)
        res = []
        if len(n1) > len(n2):
            n1,n2 = n2, n1
        for key in n1.keys():
            if key in n2:
                res += [key] * min(n1[key], n2[key])
        return res
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
a = Solution()
print(a.intersect(nums1, nums2))