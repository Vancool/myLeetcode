class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if (n == 0 or m == 0):
            if (n == 0):
                return nums1
            if (m == 0):
                return nums2
        if(nums1[m-1] < nums2[0]):
            nums1[m:m+n] = nums2
            return nums1
        elif(nums2[n-1] < nums1[0]):
            nums1[n:m+n] = nums1
            nums1[0:n] = nums2
            return nums1
        removeNum = [x for x in range(m)]
        nums2Index = [0] * n
        index = 0
        breakPoint = n
        for i in range(n):
            while index < m:
                if (nums1[index] <= nums2[i]):
                    index += 1
                else:
                    nums2Index[i] = removeNum[index]
                    removeNum[index] += 1
                    break
            if( index >= m and i < n):
                breakPoint = i
                break

        for i in range(1, m):
            if (removeNum[i-1] != i-1):
                removeNum[i] = removeNum[i] + removeNum[i - 1] - (i-1)
        for i in range(m - 1, -1, -1):
            nums1[removeNum[i]] = nums1[i]
        for j in range(n):
            if(j>= breakPoint):
                break
            nums1[nums2Index[j]] = nums2[j]
        nums1[m+breakPoint:m+n] = nums2[breakPoint: n]

        return nums1

if __name__ == "__main__":
    a = Solution()
    print(a.merge(
[0],
0,
[1],
1))
