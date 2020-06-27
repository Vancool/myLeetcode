import random
class Solution(object):
    def topKFrequent(self, nums, k):
        def quickSort(k, arr, left, right):
            if left >= right:
                ''' 注意递归的边界条件'''
                return arr[0:k]
            index = random.randint(left, right)
            arr[left], arr[index] = arr[index], arr[left]
            pivot = arr[left][0]
            l = left
            r = right
            left += 1
            while left <= right:
                while left <= right and arr[left][0] >= pivot:
                    left += 1
                while left <= right and arr[right][0] < pivot:
                    right -= 1
                if left <= right:
                    arr[left], arr[right] = arr[right], arr[left]
                    left += 1
                    right -= 1
            arr[right], arr[l] = arr[l], arr[right]
            if right == k:
                return arr[0:k]
            elif right > k:
                return quickSort(k, arr, l, right - 1)
            elif right < k:
                return quickSort(k, arr, right + 1, r)

        if len(nums) == 1:
            return nums
        key_value = {}
        value_key = []
        for n in nums:
            key_value[n] = key_value.get(n, 0) + 1
        for key, val in key_value.items():
            value_key.append((val, key))
        res = quickSort(k, value_key, 0, len(value_key) - 1)
        return [key[1] for key in res]
'''
test case1
[-1,-1]
[1, 2]
'''
if __name__ == "__main__":
    nums = [1, 2]
    k = 2
    a = Solution()
    print(a.topKFrequent(nums,k))