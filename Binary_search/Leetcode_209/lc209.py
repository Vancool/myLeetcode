
class Solution1(object):
    def minSubArrayLen(self, s, nums):
        if len(nums) == 0: return 0
        left = 0
        right = 0
        res = 0
        min_dis = len(nums) + 1
        while right < len(nums):
            res += nums[right]
            while res >= s:
                min_dis = min(right - left + 1, min_dis)
                res -= nums[left]
                left += 1
            right += 1
        return min_dis if min_dis <= len(nums) else 0

'''
最佳解法是滑动窗口
'''

'''
关于O(nlog(n)) 我的想法是分治，但是中间那一块用贪心还是有算法错误
所以O(nlog(n))的写法 没写出来
人家的写法是使用 前缀和 + 二分
https://leetcode-cn.com/problems/minimum-size-subarray-sum/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-43/
'''
class Solution(object):
    def countCrossLen(self, s, nums, left, mid, right):
        res = nums[mid]
        count = 1
        max_len = right - left + 1
        curl = mid - 1
        curr = mid + 1
        while count <= max_len or (curr <= right or curl >= left):
            if res >= s: return count
            if curl >= left and curr <= right:
                if nums[curr] >= nums[curl]:
                    res += nums[curr]
                    curr += 1
                else:
                    res += nums[curl]
                    curl -= 1
            elif curr <= right:
                res += nums[curr]
                curr += 1
            elif curl >= left:
                res += nums[curl]
                curl -= 1
            count += 1
        return 0

    def minSubArrayLen(self, s, nums):
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1 if nums[0] >= s else 0
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        leftres = self.minSubArrayLen(s, nums[left:mid + 1])
        rightres = self.minSubArrayLen(s, nums[mid + 1:right + 1])
        crossres = self.countCrossLen(s, nums, left, mid, right)
        res = len(nums) + 1
        for key in (leftres, rightres, crossres):
            if key:
                res = min(key, res)
        return res if res <= len(nums) else 0


class Solution1(object):
    def minSubArrayLen(self, s, nums):
        def binary_search(target, index, arr):
            left = index
            right = len(arr)-1
            while left <= right:
                mid = left + (right-left) // 2
                val = arr[mid] - arr[index] + nums[i]
                '''注意这边需要加一个nums[i]
                因为 sum[j] - sum[i] 会把 nums[i]减掉
                '''
                if val == target:
                    return mid
                elif val > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        if len(nums) == 0: return 0
        presum = [0] * len(nums)
        presum[0] = nums[0]
        for i in range(1, len(nums)):
            presum[i] = presum[i-1] + nums[i]
        if presum[-1] < s: return 0
        min_dis = float('inf')
        for i in range(len(nums)):
            '''其实在这边从后往前搜索会更好, 时间问题不写了'''
            right = binary_search(s, i, presum)
            if right == len(nums): continue
            min_dis = min(min_dis, right - i + 1)
        return min_dis



a = Solution1()
s = 213
nums = [12,28,83,4,25,26,25,2,25,25,25,12]
print(a.minSubArrayLen(s, nums))