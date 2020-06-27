class Solution(object):
    def nextPermutation(self, nums):
        if len(nums) == 1: return nums
        minj = -1
        mini = len(nums)
        for i in range(len(nums) - 1, 0,-1):
            for j in range(i, -1, -1):
                if nums[i] > nums[j]:
                    if minj < j:
                        minj = j
                        mini = i

                if i < minj:
                    break
        if minj != len(nums):
            nums[mini], nums[j] = nums[j], nums[mini]
            # 插入排序
            for k1 in range(j + 1, len(nums)):
                tmp = nums[k1]
                for k2 in range(k1, j, -1):
                    if nums[k2 - 1] > tmp:
                        nums[k2] = nums[k2 - 1]
                    else:
                        break
                nums[k2] = tmp
            return

        nums.reverse()
'''
下一个排列：

test case:
[5,4,7,5,3,2]
[1,3,2]
[2,2,7,5,4,3,2,2,1]
[4,2,0,2,3,2,0]
'''
'''
哈哈，这题没写对
主要是解法没想好，其实已经想到一半了但是发现自己对题目的答案想错了。
解法见other
'''
a = Solution()
n =[4,2,0,2,3,2,0]
a.nextPermutation(n)
print(n)
print("Done")