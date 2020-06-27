class Solution(object):
    def canReach(self, arr, start):
        if len(arr) == 0: return False
        if len(arr) == 1: return arr[0] == 0
        if arr[start] == 0: return True
        def dfs(start):
            if start < 0 or start >= len(arr): return False
            if arr[start] == -1: return False
            if arr[start] == 0: return True
            left = start - arr[start]
            right = start + arr[start]
            arr[start] = -1
            return dfs(left) or dfs(right)
        return dfs(start)



    '''
    我自己没想好思路，原来这个是可以看成一个图然后用图论的方式检验是否可达
    '''

a = Solution()
arr = [3,0,2,1,2]
start = 2
print(a.canReach(arr, start))