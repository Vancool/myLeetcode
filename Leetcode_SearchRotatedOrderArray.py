class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1
        if n == 1 :
            if nums[0] == target:
                return 0
            else:
                return -1
        pivot = n//2
        output = 0
        while n > 0:
            if nums[pivot] == target:
                output = output + pivot
                break
            elif nums[pivot] > target:
                if(nums[0] == target):
                    break
                if(nums[0] < target and nums[0] < nums[pivot])\
                or (nums[0] > target and nums[0] > nums[pivot]):
                    nums = nums[1:pivot]
                    output += 1
                else:
                    nums = nums[pivot+1:]
                    output += pivot+1
            elif nums[pivot] < target:
                if(nums[-1] == target):
                    output += n-1
                    break
                if(nums[-1] > target and nums[-1] > nums[pivot])\
                or (nums[-1] < target and nums[-1] < nums[pivot] ):
                    nums = nums[pivot+1:n]
                    output += pivot+1
                else:
                    nums = nums[0:pivot]
            n = len(nums)
            pivot = n//2
        if len(nums) == 0:
            return -1
        else:
            return output

if __name__ == "__main__":
    a = Solution()
    print(a.search([4,5,6,7,0,1,2],5))