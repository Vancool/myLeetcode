class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums[0] >= target:
            return []
        pos = -1
        left = 0
        right = len(nums)-1
        if left <= right:
            mid = left + (right-left)//2
            if nums[mid] >= target:
                right = mid -1
            elif nums[mid] < target:
                left = mid + 1
        pos = right
        for i in range(pos-1):
            val = target - nums[i]
            left = i + 1
            right = pos
            while left <= right:
                mid = left + (right-left) // 2
                if nums[mid] == val:
                    return [nums[i], val]
                elif nums[mid] > val:
                    right = mid -1
                else:
                    left = mid + 1
        return []

a = Solution()
nums = [14,15,16,22,53,60]
target = 76
print(a.twoSum(nums,target))
print("Done")