class Solution(object):
    def maxScoreSightseeingPair(self, A):
        res = A[0] + 0
        pre = A[0]
        for i in range(1, len(A)):
            sub_res = A[i] + i
            res = max(sub_res+pre, res)
            pre = max(pre, A[i]-i)
        return res

