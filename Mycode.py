
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for key in nums:
            dic[key] = dic.get(key, 0)+1
        for key, val in dic.items():
            if val>1:
                return key
a = Solution()
key =a.findRepeatNumber([2, 3, 1, 0, 2, 5, 3])
print("Done")