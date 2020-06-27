from collections import deque
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        if len(nums2) * len(nums1) == 0: return []
        hashmap = {}
        stack = deque()
        for i in range(len(nums2)-1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if not stack:
                hashmap[nums2[i]] = -1
            else:
                hashmap[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        nums1 = map(lambda x: hashmap[x], nums1)
        return nums1


