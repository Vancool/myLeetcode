class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if len(arr) == k:
            return arr
        if x <= arr[0]:
            return arr[0:k]
        if x >= arr[-1]:
            return arr[len(arr)-k: len(arr)]
        def binary_search(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return right

        index = binary_search(arr, x)
        '''
        此处不能是 + k-1 因为不知道index到底是不是x
        如果是x就是包含index的， 如果不是的话就有可能不包含
        因为返回的是最后一个比x小的数值，不知道小多少，所以可能不包含
        '''

        left = max(0, index-k)
        right = min(len(arr)-1, index + k)
        while right - left + 1 > k:
            if x - arr[left] > arr[right] - x:
                left += 1
            else:
                right -= 1
        return arr[left:right+1]
a = Solution()
arr = [1,2,3,4,5,6]
print(a.findClosestElements(arr, 1,2))
print("Done")