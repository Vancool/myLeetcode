class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if n == 0: return
        index1 = m-1
        index2 = n-1
        right = m+n-1
        while index1 >= 0 and index2 >= 0:
            if nums1[index1] >= nums2[index2]:
                nums1[right]  = nums1[index1]
                index1 -= 1
            else:
                nums1[right] = nums2[index2]
                index2 -= 1
            right -= 1
        while index2 >= 0:
            nums1[right] = nums2[index2]
            right -= 1
            index2 -= 1

'''
不能用交换从前往后
只能用归并的merge 从后往前

因为 test case:
[4,5,6,0,0,0]
[1,2,3]


反正我没写出来从前往后的
还是从后往前的比较简单一些。

'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if n == 0: return
        index1 = 0
        index2 = 0
        while index1 < m and index2 < n:
            if nums1[index1] > nums2[index2]:
                nums1[index1], nums2[index2] = nums2[index2], nums1[index1]
                while index2 + 1 < n and nums2[index2] > nums2[index2+1]:
                    index2 += 1
            index1 += 1
        lindex2 = 0
        rindex2 = index2
        while rindex2 < n and lindex2 < index2:
            if nums2[lindex2] >= nums2[rindex2]:
                nums1[index1] = nums2[rindex2]
                rindex2 += 1
            else:
                nums1[index1] = nums2[lindex2]
                lindex2 += 1
            index1 += 1
        while rindex2 < n:
            nums1[index1] = nums2[rindex2]
            rindex2 += 1
            index1 += 1
        while lindex2 < index2:
            nums1[index1] = nums2[lindex2]
            lindex2 += 1
            index1 += 1

a = Solution()
n1 = [-1,0,1,1,0,0,0,0,0]
n2 = [-1,0,2,2,3]
a.merge(n1,4,n2,5)
print(n1)





