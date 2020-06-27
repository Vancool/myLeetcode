class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        count = [0] * len(nums)
        for i in range(len(nums)-2, -1,-1):
            k = i + 1
            while k < len(nums) and nums[k] >= nums[i]:
                k += 1
            if k == len(nums):
                count[i] = 0
            else:
                count[i] = count[k] + 1
        return count
'''
想太简单了， 然后以为前一个就是之前所有的相加后面那个
总之这题我还是不会做
'''

a = Solution()
num = [5,5,5,5]
print(a.countSmaller(num))
print("Done")


