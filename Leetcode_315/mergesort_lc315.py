class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return  [0]
        '''
        使用归并算法求逆序对用来求右边有多少个小的数
        '''
        res = [0] * len(nums)
        arr = []
        tmp = [None for _ in range(len(nums))]
        for i in range(len(nums)):
            arr.append((nums[i], i))
        def merge_sort(left, right, arr):
            if left == right:
                return
            mid = left + (right-left) // 2
            merge_sort(left, mid, arr)
            merge_sort(mid+1, right, arr)
            merge_arr(left, mid, right)

        def merge_arr(left, mid, right):
            if arr[mid][0] <= arr[mid+1][0]:
                return
            l,r = 0,0
            tmpIndex = left
            while l+left <= mid and mid+1+r <= right:
                leftIndex = left + l
                rightIndex = mid+1+r
                if arr[leftIndex][0] <= arr[rightIndex][0]:
                    tmp[tmpIndex] = arr[leftIndex]
                    res[arr[leftIndex][1]] += r
                    l += 1
                else:
                    tmp[tmpIndex] = arr[rightIndex]
                    r += 1
                tmpIndex += 1

            while l+left <= mid:
                leftIndex = left + l
                tmp[tmpIndex] = arr[leftIndex]
                res[arr[leftIndex][1]] += r
                l += 1
                tmpIndex += 1

            while r+mid+1<= right:
                rightIndex = mid + 1 + r
                tmp[tmpIndex] = arr[rightIndex]
                tmpIndex += 1
                r += 1
            while right >= left:
                arr[right] = tmp[right]
                right -= 1

        merge_sort(0,len(arr)-1, arr)
        return res

a = Solution()
num = [0,2,1]
print(a.countSmaller(num))
print("Done")










