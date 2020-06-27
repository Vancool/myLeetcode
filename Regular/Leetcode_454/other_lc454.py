class Solution(object):
    def fourSumCount(self, A, B, C, D):
        if not (A and B and C and D): return 0
        A.sort()
        B.sort()
        C.sort()
        D.sort()
        if A[0] + B[0] + C[0] + D[0] > 0: return 0
        if A[-1] + B[-1] + C[-1] + D[-1] < 0: return 0
        hashAB = {}
        hashCD = {}
        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                AB = A[i] + B[j]
                CD = C[i] + D[j]
                hashAB[AB] = hashAB.get(AB, 0) + 1
                hashCD[CD] = hashCD.get(CD, 0) + 1
        for key, value in hashAB.items():
            if -key in hashCD:
                res += value * hashCD[-key]
        return res


'''
四个数组的和其实就是可以合成两个哈希表的两数之和
就变成了哈希表求解 O(n)
'''