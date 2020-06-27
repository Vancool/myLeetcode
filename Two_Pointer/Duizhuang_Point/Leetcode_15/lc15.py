class Solution(object):
    def threeSum(self, nums):
        if len(nums) <= 2:
            return []
        nums = sorted(nums)
        if nums[0] > 0 or nums[-1] < 0:
            return []
        res = []
        for i in range(len(nums)-2):
            if nums[i] > 0 :
                break
            if i >0 and nums[i] == nums[i-1]:
                continue
            target = - nums[i]
            left = i + 1
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] == target:
                    '''
                    我这个位置处理得不好，应该跳过之后所有重复的才对，我是这么写的：
                 if left-1 == i or (left > 0 and nums[left-1]!= nums[left]):   
                        res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1   
                但是其实应该是下面这种写法会更好
                    '''
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif nums[left] + nums[right] > target:
                    if nums[left] > target:
                        break

                    right -= 1
                elif nums[left] + nums[right] < target:
                    if nums[right] < 0:
                        break
                    left += 1
        return res
'''
3 Sum
https://leetcode-cn.com/problems/3sum/
test case:
[0,-4,-1,-4,-2,-3,2]
[0,0,0,0,0,0]
'''
a = Solution()
nums = [0,0,0,0,0,0]
print(a.threeSum(nums))
print("Done")

