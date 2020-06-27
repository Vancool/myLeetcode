class Solution(object):
    def findNumberOfLIS(self, nums):
        if len(nums) < 2: return len(nums)
        dp = [1] * len(nums)
        dp_len = [1] * len(nums)
        res = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] == dp[j] + 1:
                        dp_len[i] += dp_len[j]
                    elif dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        dp_len[i] = dp_len[j]
            '''
            不要先算 长度再来一次循环 统计有多少个
            if dp[i] == 1:
                dp_len[i] = 1
            else:
                for j in range(i):
                    if nums[i] > nums[j]:
                        if dp[j] == dp[i] - 1:
                            dp_len[i] += dp_len[j]
            会比较慢
            '''
            res = max(res, dp[i])
        count = 0
        for i in range(len(dp)):
            if dp[i] == res:
                count += dp_len[i]
        return count

'''
贪婪 + 2分解法
'''
class Solution1(object):
    def findNumberOfLIS(self, nums):
        def binary_search(key, len_vec, is_row, pre):
            if is_row:
                left = 0
                right = len(len_vec) - 1
            else:
                left = 0
                right = len(len_vec[pre])-1
            while left <= right:
                mid = left + (right - left) // 2
                if is_row:
                    val = len_vec[mid][-1][0]
                    if val == key:
                        return mid
                    elif val < key:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    val = len_vec[pre][mid][0]
                    if val == key:
                        return mid
                    elif val < key:
                        right = mid -1
                    else:
                        left = mid + 1
            return left
        if len(nums) < 2: return len(nums)
        len_greedy = []
        len_greedy.append([(nums[0],1)])
        for i in range(1,len(nums)):
            if nums[i] > len_greedy[-1][-1][0]:
                pos = len(len_greedy)
            else:
                pos = binary_search(nums[i], len_greedy, True,0)
            count = 1 #要提前赋值
            if pos > 0: # 这边要注意， 如果插入的是第一个直接append 不用找前一个的二分
                pre = pos - 1
                pre_index = binary_search(nums[i],len_greedy, False, pre) # 可能有很多个重复
                while len_greedy[pre][pre_index][0] == nums[i]: pre_index += 1
                if pre_index == 0: count = len_greedy[pre][-1][1]
                else: count = len_greedy[pre][-1][1] - len_greedy[pre][pre_index-1][1]
            if pos == len(len_greedy):
                len_greedy.append([(nums[i], count)])
            else:
                len_greedy[pos].append((nums[i], count + len_greedy[pos][-1][1]))
        return len_greedy[-1][-1][1]
'''
二分法每次都会卡这个test case:
就是存在相等的数的时候怎么处理
[1,2,4,3,5,4,7,2]
[1,4,1,3,1,-14,1,-13]
'''
a = Solution1()
nums = [1,4,1,3,1,-14,1,-13]
print(a.findNumberOfLIS(nums))