class Solution(object):
    def maxScoreSightseeingPair(self, A):
        left = 0
        right = len(A)-1
        res = 0
        while left < right:
            res = max(res, (left-right+A[left]+A[right]))
            if A[left] < A[right]:
                left += 1
            elif A[left] > A[right]:
                right -= 1
            else:
                tmpleft = left
                tmpright = right
                while left < right and A[left] == A[right]:
                    left += 1
                    right -= 1
                #    res = max(res, left-right+A[left]+A[right])
                if A[left] <= A[right]:
                    right = tmpright
                else:
                    left = tmpleft
        return res


'''
test case:
[3,7,2,3]
'''
'''
这题不能用双指针， 双指针是针对一个变大一个变小两个变量用的
而这个如果是两个同时变大，不知道哪个大的程度更高，就会出错
如果两个同时变大，那么可以找其中一个不变的变量然后求下一个， 看求下一个有没有优化方法
这一题就是 A[j] + A[i] + j - i
那么可以分类成 A[j]+j + A[i]-i (i > j)
'''
a = Solution()
nums = [3,7,2,3]
print(a.maxScoreSightseeingPair(nums))