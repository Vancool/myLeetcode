class Solution(object):
    def canReach(self, arr, start):
        if len(arr) == 0: return False
        if len(arr) == 1: return arr[0] == 0
        if arr[start] == 0: return True
        while True:
            change = False
            for i in range(len(arr)):
                if arr[i] == 0: continue
                left = i - arr[i]
                right = i + arr[i]
                if (left >= 0 and arr[left] == 0) or (right < len(arr) and arr[right] == 0):
                    arr[i] = 0
                    change = True
                    if i == start: return True
            if not change: break
        return False


a = Solution()
arr = [3,0,2,1,2]
start = 2
print(a.canReach(arr, start))


