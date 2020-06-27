class Solution(object):
    def sortColors(self, nums):
        def sortNumber(left, right, number):
            while left <= right:
                while left <= right and nums[left] != number:
                    left += 1
                while left <= right and nums[right] == number:
                    right -= 1
                if left <= right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
            return right
        if len(nums) <= 1:
            return nums
        left, right = 0, len(nums) - 1
        left, right = 0, sortNumber(left, right, 2)
        sortNumber(left, right, 1)
        return nums


'''
https://leetcode-cn.com/problems/sort-colors/
一开始的想法，找某个数字的位置放在它该在的位置

但是其实这个就是快排的思想的partition过程：
给一个数，前面都是比它大的，后面都是比它小的
与快排的区别，因为知道只有三个数， 所以有三个index, 分别对应于只有0的区， 只有1的区和只有2的区
[0:zero] 只有0
（zero, i）只有1
[two:] 只有2

总之，涉及到分区： 快排思想
'''
class Solution(object):
    def sortColors(self, nums):
        if len(nums) <= 1:
            return nums
        zero = -1
        i = 0
        two = len(nums) - 1
        while i <= two:
            if nums[i] == 0:
                zero += 1
                nums[i], nums[zero] = nums[zero], nums[i]
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[i], nums[two] = nums[two], nums[i]
                #这个时候不知道i是不是1，所以不能 i++
                two -= 1
        return nums



'''
test case:
1.
[2,1]
'''
if __name__ == "__main__":
    a = Solution()
    nums = [1,2,1]
    print(a.sortColors(nums))

