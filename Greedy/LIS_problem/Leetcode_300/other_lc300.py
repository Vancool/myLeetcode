class Solution(object):
    def lengthOfLIS(self, nums):
        if len(nums) == 0: return 0

        def binary_search(key):
            left = 0
            right = len(minGreedy)-1
            while left <=  right:
                mid = left + (right - left)//2
                if minGreedy[mid] == key:
                    return mid
                elif minGreedy[mid] > key:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        minGreedy = []
        minGreedy.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] > minGreedy[-1]:
                minGreedy.append(nums[i])
            else:
                pos = binary_search(nums[i])
                minGreedy[pos] = nums[i]
        return len(minGreedy)

'''
解 LIS（longest increasing subsequence） 问题
两种方法： DP 和 greedy+2分查找

DP 可以在任何场景下适用 缺点是时间复杂度 O(n^2)
greedy + 2分 只能求一个最长上升字串长度 or 具体路径, 时间复杂度O(nlog(n))

如果是要求出具体的所有的最长字串的话两种方法的时间复杂度是一样的 O(n^3)
'''


