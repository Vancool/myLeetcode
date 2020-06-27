class Solution(object):
    def fourSumCount(self, A, B, C, D):
        if not (A and B and C and D): return 0
        A.sort()
        B.sort()
        C.sort()
        D.sort()
        if A[0] + B[0] + C[0] + D[0] > 0: return 0
        if A[-1] + B[-1] + C[-1] + D[-1] < 0: return 0
        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                value = -(A[i] + B[j])
                if value > D[-1] + C[-1]: continue
                if value < D[0] + C[0]: continue
                left = 0
                right = len(D)-1
                while left < len(C) and right >= 0:
                    tmp = C[left] + D[right]
                    if tmp == value:
                        res += 1
                        left += 1
                        while left < len(C) and C[left] == C[left-1]:
                            res += 1
                            left += 1
                        right -= 1
                        while right >= 0 and D[right] == D[right+1]:
                            res += 1
                            right -= 1
                    elif tmp > value:
                        right -= 1
                    else:
                        left += 1
        return res

'''
为啥我会想着用双指针555
没解出来
'''


a = Solution()
A = [0,1,-1]
B = [-1,1,0]
C = [0,0,1]
D = [-1,1,1]
print(a.fourSumCount(A,B,C,D))
