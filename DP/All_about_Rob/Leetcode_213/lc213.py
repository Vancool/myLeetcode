class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) <= 3:
            return max(nums)
        def Helper(start, end, nums):
            cur, pre = 0, 0 #这个操作相当于在数组前面加了两个0元素做起始
            for i in range(start, end+1):
                tmp_cur = max(pre+nums[i], cur)
                pre = cur
                cur = tmp_cur
            return cur
        return max(Helper(0,len(nums)-2,nums), Helper(1,len(nums)-1,nums))



'''
一开始的想法：有没有用第一个用一个flag来表示，但是不行，因为不知道第三个如果够大就还会用，还是要看后续的数考虑用不用nums[0]
test case:
[1,1,1,1,1]
[2,7,9,3,1]

想到了做两次dp，觉得很不hack所以看了答案
果然还是做两次dp
'''

a = Solution()
nums = [2,7,9,3,1]
print(a.rob(nums))
print("Done")