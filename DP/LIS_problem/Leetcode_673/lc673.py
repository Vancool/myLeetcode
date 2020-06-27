class Solution(object):
    def findNumberOfLIS(self, nums):
        if len(nums) < 2: return len(nums)
        max_len = 1
        dp = [1] * len(nums)
        res = [[] for _ in range(len(nums))]
        res[0] = [[nums[0]]]
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] == 1:
                res[i].append([nums[i]])
            else:
                for j in range(i):
                    if nums[j] < nums[i] and dp[j] == dp[i]-1:
                        for path in res[j]:
                            res[i].append(path + [nums[i]])
            max_len = max(max_len, dp[i])
        count = 0
        if max_len == 1:
            return len(nums)
        else:
            for i in range(len(nums)):
                if max_len == dp[i]:
                    count += len(res[i])
        return count

class Solution1(object):
    def findNumberOfLIS(self, nums):
        def binary_search(key):
            left = 0
            right = len(min_element)-1
            while left <=  right:
                mid = left + (right - left)//2
                if min_element[mid] == key:
                    return mid
                elif min_element[mid] > key:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        if len(nums) < 2: return len(nums)
        min_element = [nums[0]]
        path = [[[nums[0]]]]
        for i in range(1,len(nums)):
            if min_element[-1] < nums[i]:
                min_element.append(nums[i])
                subpath = []
                for p in path[-1]:
                    if p[-1] < nums[i]:
                        subpath.append(p + [nums[i]])
                path.append(subpath)
            else:
                pos = binary_search(nums[i])
                min_element[pos] = nums[i]

                if pos == 0:
                    path[pos].append([nums[i]])
                else:
                    for p in path[pos-1]:
                        if p[-1] < nums[i]:
                            path[pos].append(p + [nums[i]])
        return len(path[-1])


'''
test case:
nums = [1,2,4,3,5,4,7,2]
'''
'''
我自己写得还是复杂了
因为我自己把所有的数组都算出来了，还加上了对所有字符串遍历复制的时间
其实没必要。
'''
a = Solution1()
nums =[2,2,2,2,3]
print(a.findNumberOfLIS(nums))
