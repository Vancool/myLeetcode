class Solution1(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        if len(a) == 0:
            return []
        if len(a) == 1:
            return 1
        leftDp = [0]*len(a)
        leftDp[0] = 1
        rightDp = [0] * len(a)
        rightDp[-1] = 1
        for i in range(1,len(a)):
            leftDp[i] = leftDp[i-1] * a[i-1]
        for i in range(len(a)-2,-1,-1):
            rightDp[i] = rightDp[i+1] * a[i+1]
        for i in range(len(a)):
            leftDp[i] *= rightDp[i]
        return leftDp
    '''
    像这样的对称的题目，最好就是求两个从左和从右的对称数组，然后找规律
    
    这一题对应着leetcode 238
    实际上题目还要求我们将空间复杂度降低为O(1)【不算输出数组的空间】
    '''

class Solution(object):
    def productExceptSelf(self, nums):
        res = [0] * len(nums)
        if  len(res) == 0:
            return res
        res[0] = 1
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        temp = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = temp * res[i]
            temp *= nums[i]
        return res
a = Solution()
print(a.productExceptSelf([1,2,3,4]))
print("Done")
