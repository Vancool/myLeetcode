class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        n = len(nums)
        flag = [0] * 100
        sortedNums = sorted(nums)  # O(nlog(n))
        targetIndex = n
        for i in range(n):
            if target - sortedNums[0] > sortedNums[i]:
                targetIndex = i - 1
                break

        minIndex = 0
        maxIndex = targetIndex
        k = (targetIndex - minIndex + 1) / 2
        while n != 0:
            while (k < maxIndex) and (k > minIndex):
                if (soredNums[minIndex] + sortedNums[k] == target):
                    result.append()
