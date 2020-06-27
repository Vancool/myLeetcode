class Solution(object):
    def findBestValue(self, arr, target):
        arr.sort()
        n = len(arr)
        i = 0
        aver = arr[0]
        while n > 0:
            aver = target/n
            if arr[i] >= aver: return int(aver) if aver - int(aver) <= 0.5 else int(aver)+1
            target -= arr[i]
            i += 1
            n -= 1
        return arr[-1]

'''
其实仔细一看就是前缀和的思路
'''
class Solution(object):
    def findBestValue(self, arr, target):
        arr.sort()
        pre = 0
        for i, num in enumerate(arr):
            aver = (target-pre) / (len(arr)-i)
            if arr[i] >= aver: return int(aver) if aver - int(aver) <= 0.5 else int(aver)+1
            pre += arr[i]
        return arr[-1]

'''
另一种 枚举平均值思路
这个是不需要排序的，但是要每次都要算sum
'''
class Solution(object):
    def findBestValue(self, arr, target):
        aver = target / len(arr)
        value = int(aver)
        pre_count = 0
        count = 0
        for num in arr:
            count += num if num <= value else value
        max_value = max(arr)
        while count < target:
            pre_count = count
            count = 0
            for num in arr:
                count += num if num <= value else value
            value += 1
            if value >= max_value:
                return max_value
        return value-1 if abs(target-count) < abs(target-pre_count) else value-2


'''
另一种加的思路，要排序
'''
# class Solution(object):
#     def findBestValue(self, arr, target):
#         arr.sort()
#         pre = 0
#         for i, num in enumerate(arr):
#             if pre + num * (len(arr)-i) < target:
#                 pre += num
#             else:
#                 aver = (pre + num*(len(arr)-i)-target)/(len(arr)-i)
#                 return num - round(aver+0.00001)
#         return arr[-1]


# class Solution(object):
#     def findBestValue(self, arr, target):
#         summ = sum(arr)
#         if summ <= target:
#             return max(arr)
#         l = len(arr)
#         val = target // l
#         summ, last = val * l, 0
#         while summ < target:
#             last = summ
#             summ = 0
#             for i in range(l):
#                 summ += arr[i] if val > arr[i] else val
#             val += 1
#         return val - 2 if abs(target - summ) >= abs(target - last) else val - 1


a = Solution()
arr = [1,2,3,4,10000000]
t = 1000
print(a.findBestValue(arr, t))
