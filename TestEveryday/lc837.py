class Solution(object):
    def new21Game(self, N, K, W):
        if K > N or K - 1 + W < N: return 0.0
        if K == 1: return 1.0