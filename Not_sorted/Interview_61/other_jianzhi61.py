'''
不排序的O(n)方法

'''
class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = set()
        maxVal = 0
        minVal = 100000
        for n in nums:
            if n == 0:
                continue
            if n in dic:
                return False
            dic.add(n)
            maxVal = max(maxVal, n)
            minVal = min(minVal, n)
        if len(nums) < maxVal - minVal + 1:
            return False
        return True
    '''
    因为面试官可能会问求是否是顺子的不排序方法
    其实如果是顺子除了0之外我们可以假设它是个等差数列
    那么 max - min +1 如果是<= 5的话说明相差只有5或者比5小很多0，如果里面没有重复的话就是True
    如果比5大的话说明差距没有办法用0弥补，因为最多也就5个0
    
    还挺像脑筋急转弯的。
    '''