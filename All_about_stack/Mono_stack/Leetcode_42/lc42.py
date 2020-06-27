class Solution(object):
    def trap(self, height):
        if len(height) <= 2:
            return 0
        visited = set()
        res = 0
        maxIndex = -1
        for i in range(len(height)):
            if height[i] != 0:
                if maxIndex == -1:
                    maxIndex = i
                    visited.add(i)
                elif height[maxIndex] <= height[i]:
                    res += height[maxIndex] * (i-maxIndex-1)
                    for j in range(maxIndex+1, i):
                        res -= height[j]
                    visited.add(i)
                    maxIndex = i
        maxIndex = len(height)
        for i in range(len(height)-1,-1,-1):
            if height[i] != 0:
                if maxIndex == len(height):
                    maxIndex = i
                elif height[maxIndex] <= height[i] and not(i in visited and maxIndex in visited):
                    res += height[maxIndex] * (maxIndex - i -1)
                    for j in range(maxIndex-1, i, -1):
                        res -= height[j]
                    visited.add(maxIndex)
                    maxIndex = i
        return res

'''
test case:
1. [4,9,4,5,3,2]
'''
a = Solution()
h =[0,1,0,2,1,0,1,3,2,1,2,1]
print(a.trap(h))
print("Done")


