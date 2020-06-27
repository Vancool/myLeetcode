import random
class Solution(object):
    def findKthLargest(self, nums, k):
        def partition(left, right, arr):
            if left >= right:
                return right
            index = random.randint(left, right)
            arr[left], arr[index] = arr[index], arr[left]
            pivot = arr[left]
            l = left + 1
            r = right
            while l <= r:
                while l <= r and  arr[l] >= pivot:
                    l += 1
                while l <= r and arr[r] < pivot:
                    r -= 1
                if l <= r:
                    arr[l], arr[r] = arr[r], arr[l]
                    l += 1
                    r -= 1
            arr[r], arr[left] = arr[left], arr[r]
            return r # pivot index
        def quicksort(left, right, k, arr):
            index = partition(left, right, arr)
            if k == index:
                return arr[k]
            elif k < index:
                return quicksort(left, index-1, k, arr)
            elif k > index:
                return quicksort(index+1, right, k, arr)

        if k == len(nums) or len(nums) <= 1:
            return max(nums)
        res = quicksort(0, len(nums)-1, k-1, nums)
        return res
'''
快排topK 
平均时间复杂度 O(n)
最坏时间复杂度O(n^2)
有人总结了
这个人总结得挺好的
https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/3chong-jie-fa-miao-sha-topkkuai-pai-dui-er-cha-sou/
'''
a = Solution()
nums =  [3,2,3,1,2,4,5,5,6]
k = 4
print(a.findKthLargest(nums, k))