class Solution1(object):
    def reversePairs(self, nums):
        if len(nums) == 0 or len(nums) == 1: return 0
        res = 0
        for i in range(1,len(nums)):
            tmp = nums[i]
            for j in range(i, -1, -1):
                if j > 0 and nums[j-1] > tmp:
                    res += 1
                    nums[j] = nums[j-1]
                else: break
            nums[j] = tmp
        return res
'''
概念， 插入和冒泡这两种交换相邻的，可以每次消去一个逆序对
但是其实这样和枚举暴力求解没有区别
'''
'''
归并排序加速 寻找逆序对
归并排序的两种写法：
'''
# 递归
class Solution2(object):
    def reversePairs(self, nums):
        if len(nums) == 0 or len(nums) == 1: return 0
        temp = [0] * len(nums)
        def count_crossNum(nums, left, mid, right):
            if nums[mid] <= nums[mid+1]:
                return 0
            l = left
            r = mid+1
            res = 0
            index = left
            #因为最后换到 nums 里，所以从temp 倒过去
            while left <= right:
                temp[left] = nums[left]
                left += 1
            while l <= mid  and r <= right:
                if temp[l] <= temp[r]:
                    nums[index] = temp[l]
                    l += 1
                elif temp[r] < temp[l]:
                    res += mid-l+1
                    nums[index] = temp[r]
                    r += 1
                index += 1
            #归并是while循环啊
            while l <= mid:
                nums[index] = temp[l]
                index += 1
                l += 1
            return res

        def merget_sort(nums, left, right):
            if left == right:
                return 0
            mid = left  + (right - left) // 2
            l_num = merget_sort(nums, left, mid)
            r_num = merget_sort(nums, mid+1, right)
            cross_num = count_crossNum(nums, left,mid, right)
            return l_num + r_num + cross_num

        return merget_sort(nums,0, len(nums)-1)

#循环
class Solution(object):
    def reversePairs(self, nums):
        if len(nums) == 0 or len(nums) == 1: return 0
        temp = [0] * len(nums)
        def merge(left,mid, right, nums, temp):
            if mid == right or nums[mid] <= nums[mid+1]:
                while left <= right:
                    temp[left] = nums[left]
                    left += 1
                return 0
            res = 0
            l = left
            r = mid+1
            index = left
            while l <= mid and r <= right:
                if nums[l] <= nums[r]:
                    temp[index] = nums[l]
                    l += 1
                else:
                    temp[index] = nums[r]
                    r += 1
                    res += mid-l+1
                index += 1
            while l <= mid:
                temp[index] = nums[l]
                index += 1
                l += 1
            while r <= right:
                temp[index] = nums[r]
                index += 1
                r += 1
            return res
        res = 0
        size = 1
        while size < len(nums):
            i = 0
            while i < len(nums) - 2*size:
                res += merge(i, i+size-1, i+2*size-1, nums, temp)
                i += 2*size
            if i + size - 1 < len(nums)-1:
                res += merge(i, i+size-1, len(nums)-1, nums, temp)
            else:
                res += merge(i, len(nums)-1, len(nums)-1, nums, temp)

            size *= 2
            i = 0
            while i < len(nums) - 2*size:
                res += merge(i, i+size-1, i+2*size-1, temp, nums)
                i += 2*size
            if i + size-1 < len(nums)-1:
                res += merge(i, i+size-1, len(nums)-1, temp, nums)
            else:
                res += merge(i, len(nums)-1, len(nums)-1, temp, nums)
            size *= 2

        return res









'''
test case:
[2147483647,2147483647,-2147483647,-2147483647,-2147483647,2147483647]
'''
a = Solution()
nums = [2147483647,2147483647,-2147483647,-2147483647,-2147483647,2147483647]
print(a.reversePairs(nums))
