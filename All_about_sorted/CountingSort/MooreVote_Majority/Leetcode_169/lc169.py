class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

import random
class Solution(object):
    def majorityElement(self, nums):
        def partition(left, right):
            if left >= right: return left
            # index = random.randint(left, right)
            # nums[left], nums[index] = nums[index], nums[left]
            pivot = nums[left]
            l = left + 1
            r = right
            while l <= r:
                while l <= r and nums[l] <= pivot:
                    l += 1
                while l <= r and nums[r] > pivot:
                    r -= 1
                if l <= r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
            nums[left], nums[r] = nums[r], nums[left]
            return r
        def quick_search(k, left, right):
            index = partition(left, right)
            if k == index: return nums[index]
            if k > index:
                return quick_search(k, index + 1, right)
            else:
                return quick_search(k, left, index - 1)

        return quick_search(len(nums)//2, 0, len(nums)-1)

'''
不知道为啥用 top K 的解法超时了

另一种解法： 摩尔计数
'''

class Solution(object):
    def majorityElement(self, nums):
        curnum = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                curnum = nums[i]
                count = 1
                continue
            if nums[i] == curnum:
                count += 1
            else:
                count -= 1
        return curnum
