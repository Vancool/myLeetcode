class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums)==0:
            return -1
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left+((right-left)>>1)
            if nums[mid] > nums[right]:
                left = mid+1
            elif nums[mid] <nums[right]:
                right = mid
            else:
                '''如果和right相等的情况，right往前走，反正mid和right值相同
                但是最好不要移动 mid， 因为不知道下次搜索的区间在左边还是右边'''
                right -= 1
        return nums[left]