class Solution(object):
    def wiggleMaxLength(self, nums):
        if len(nums) <= 1: return len(nums)
        up = 1
        down = -1
        pre = [(1,nums[0],0), (0,0,0)]
        cur = [(0,0,0) for _ in range(2)]
        for i in range(1,len(nums)):
            if pre[0][-1] == 0:
                if nums[i] > nums[i-1]:
                    cur[0][-1] = 1
                elif nums[i] < nums[i-1]:
                    cur[0][-1] = -1
                cur[0][0] = 1
                cur[0][1] = nums[i]
                cur[1] = pre[0]
            elif pre[0][-1] >= 1:
                if nums[i] > nums[i-1]:
                    cur[0][0] = pre[0][0] + 1
                    cur[0][1] = nums[i]
                    cur[0][2] = -1
                    if pre[0][-1] == pre[1][-1]:
                        if pre[0][-1] == 1:
                            if pre[1] < pre[2]:
                                pass

'''
自己用状态写没写出来
'''

