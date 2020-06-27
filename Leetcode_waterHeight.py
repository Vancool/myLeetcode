class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 2:
            if (height[0] > height[1]):
                return height[1]
            else:
                return height[0]
        sortH = sorted(height)
        n = len(sortH)
        print(n)
        maxValue1 = sortH[n - 1]
        Index1 = self.findValue(maxValue1, height)  # left-first maxValue1
        maxValue2 = sortH[n - 2]
        Index2 = self.findValue(maxValue2, height[::-1])  # right-first maxValue2
        Index2 = n - Index2 - 1
        if Index2 > Index1:
            temp = Index1
            Index1 = Index2
            Index2 = temp
        H = Index1 - Index2  # let Index1 always greater than Index2
        # InsideNum = height[Index2:Index1+1]
        sortH = sortH[::-1]
        print(sortH)
        for i in sortH[2:]:
            IndexTemp1 = self.findValue(i, height)
            IndexTemp2 = self.findValue(i, height[::-1])
            IndexTemp2 = n - IndexTemp2 - 1

            if ((IndexTemp1 >= Index2) and \
                        (IndexTemp1 <= Index1) and \
                        (IndexTemp2 >= Index2) and \
                        (IndexTemp2 <= Index1)):
                continue
            else:
                if maxValue2 * H < i * (Index1 - IndexTemp1):
                    maxValue2 = i
                    Index2 = IndexTemp1
                    H = Index1 - IndexTemp1

                if maxValue2 * H < i * (IndexTemp2 - Index2):
                    Index1 = IndexTemp2
                    maxValue2 = i
                    H = IndexTemp2 - Index2
                print(Index2, Index1, height[Index2], height[Index1])
        return maxValue2 * H

    def findValue(self, value, nums):
        a = len(nums)
        for i in range(a):
            if nums[i] == value:
                return i

if __name__ == "__main__":
    a = Solution()
    k = a.maxArea([76,155,15,188,180,154,84,34,187,142,22,5,27,183,111,128,50,58,2,112,179,2,100,111,115,76,134,120,118,103,31,146,58,198,134,38,104,170,25,92,112,199,49,140,135,160,20,185,171,23,98,150,177,198,61,92,26,147,164,144,51,196,42,109,194,177,100,99,99,125,143,12,76,192,152,11,152,124,197,123,147,95,73,124,45,86,168,24,34,133,120,85,81,163,146,75,92,198,126,191])
    print(k)