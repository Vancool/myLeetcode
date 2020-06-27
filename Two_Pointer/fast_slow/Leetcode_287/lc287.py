class Solution(object):
    def findDuplicate(self, nums):
        if len(nums) <= 2: return nums[0]
        fast = 0
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow: break
        slow = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return fast
'''
这题我不会做， 有三种解法
数组转链表 + 快慢指针
二分
位运算（位运算很难想，只是了解就算了
'''

'''
数组转链表是因为它已经说明了 n+1 个元素的数组 所有的元素都在 [1,n]的范围内
所以下标肯定不会超过范围，而最后构造的链表的开头就是的重复元素
（因为只有一个重复元素所以不会有走不到那个元素的情况[1,1,1,2,2,2,2]，因为不存在0元素的下标指针（除非自己指定）
所以不可能出现[4,2,2,2,0]这种单元素的自闭环

所以用快慢指针这个条件还是蛮严苛的
'''

'''
但是如果使用二分法， [4,2,2,2,0,2]这种范围在[0,4]的六个数的数组还是可以求出来的
只要指定的范围和数组满足 抽屉原理 就好
weiwei哥的二分题解我觉得很不错
https://leetcode-cn.com/problems/find-the-duplicate-number/solution/er-fen-fa-si-lu-ji-dai-ma-python-by-liweiwei1419/
'''
class Solution1(object):
    def findDuplicate(self, nums):
        def count_eq_smaller(target):
            res = 0
            for val in nums:
                if val <= target: res += 1
            return res

        if len(nums) <= 2: return nums[0]
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            count = count_eq_smaller(mid)
            if count > mid:
                right = mid
            elif count <= mid:
                left = mid + 1
        return left


a = Solution1()
nums = [1,1,1,1]
print(a.findDuplicate(nums))
