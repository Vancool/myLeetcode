class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if (len(nums) <= 3):
            return sum(nums)
        divideTarget = target * 1.0 / 3
        for i in range(len(nums)):
            nums[i] -= divideTarget

        nums = sorted(nums)
        if (nums[0] >= 0):
            return nums[0] + nums[1] + nums[2]

        if (nums[len(nums) - 1] <= 0):
            return nums[-1] + nums[-2] + nums[-3]
        index = 0
        for index in range(len(nums)):
            if nums[index] >= 0:
                break
        NegNums = nums[0:index]
        PosNums = nums[index:]
        minSum = float('inf')
        result = target
        for i in range(len(NegNums)):
            for j in range(len(NegNums)):
                if (i < j):
                    val = -(NegNums[i] + NegNums[j])
                else:
                    continue
                for pos in PosNums:
                    if val == pos:
                        return target
                    curVal = max(val, pos) - min(val, pos)
                    if (minSum > curVal):
                        minSum = curVal
                        print(-val + pos + target)
                        result = int(-val + pos + target)
        for i in range(len(PosNums)):
            for j in range(len(PosNums)):
                if (i < j):
                    val = PosNums[i] + PosNums[j]
                else:
                    continue
                for neg in NegNums:
                    if val == -neg:
                        return target
                    curVal = max(val, -neg) - min(val, -neg)
                    if curVal < minSum:
                        minSum = curVal
                        result = int(val + neg + target)
        return result

if __name__ == "__main__":
    a = Solution()
    print(a.threeSumClosest([-3,-2,-5,3,-4], -1))