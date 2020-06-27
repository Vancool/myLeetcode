class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n < 3:
            return []
        if(n == 3):
            if(sum(nums) == 0):
                return [nums]
            else:
                return []
        nums.sort()
        if(nums[0] > 0):
            return []
        if(nums[n-1] < 0):
            return []
        result = []
        for i in range(n):
            if(i!=0 and nums[i]==nums[i-1]):
                continue
            if(nums[i] >0):
                break
            left = i+1
            right = n-1
            while(left < right):
                val = nums[i] + nums[left] + nums[right]
                if(val > 0):
                    right -= 1
                elif(val < 0):
                    left += 1
                else:
                    result = result + [[nums[i], nums[left], nums[right]]]
                    left += 1
                    right -= 1
                    while(nums[left] == nums[left-1]):
                        left = left+1
                    while (nums[right] == nums[right+1]):
                        right = right-1
        return result


if __name__ == "__main__":
    a = Solution()
    k = a.threeSum([0, 0,0,0])
    print(k)