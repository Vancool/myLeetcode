from collections import defaultdict
'''
基数排序 + 快排思路
'''
class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 0:
            return ""
        if len(nums) == 1:
            return str(nums[0])
        tank = defaultdict(list)
        nums = map(str, nums)
        for key in nums:
            tank[key[0]].append(key)

        def quick_sort(nums, left, right):
            if left >= right:
                return
            pivot = nums[left]
            l = left
            r = right
            while l < r:
                while l < r and nums[r] + pivot >= pivot + nums[r]:
                    r -= 1
                if l < r :
                    nums[l] = nums[r]
                while l < r and nums[l] + pivot <= pivot + nums[l]:
                    l += 1
                if l < r:
                    nums[r] = nums[l]
            nums[l] = pivot
            quick_sort(nums,left, l-1)
            quick_sort(nums, r+1, right)
        res = []
        for i in range(10):
            if str(i) in tank.keys():
                if len(tank[str(i)]) > 1:
                    quick_sort(tank[str(i)], 0, len(tank[str(i)])-1)
                res += tank[str(i)]
        return "".join(res)





