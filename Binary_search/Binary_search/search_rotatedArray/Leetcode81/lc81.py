class Solution(object):
    def search(self, nums, target):
        if len(nums) == 0:
            return False
        left = 0
        right = len(nums) - 1
        while left <= right:
            if left == right:
                return True if nums[left] == target else False
            mid = left +((right - left) >> 1)
            if nums[mid] == target:
                return True
            while left < mid and nums[mid] == nums[left]:
                left += 1
            if left == mid:
                left = mid + 1
                continue
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


'''

https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/
个人觉得自己的代码已经很简洁了，居然还有更简洁的。
不建议模仿，但是这个代码我觉得很棒。
就是看target塞不塞得到左右区间里面，优化判断逻辑
'''
class Solution2(object):
    def search(self, nums, target):
        low=0;high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if(nums[mid]==target):
                return True
            if(nums[mid]>=nums[low]):
                if nums[low]<=target<=nums[mid]:
                    high=mid-1
                else:
                    low=low+1
            elif nums[mid]<=nums[high]:
                if nums[mid]<=target<=nums[high]:
                    low=mid+1
                else:
                    high=high-1
        return False

'''test case
1. [2,5,6,0,0,1,2]
'''
a = Solution()
nums = [2,5,6,0,0,1,2]
print(a.search(nums,0))
print("Done")
