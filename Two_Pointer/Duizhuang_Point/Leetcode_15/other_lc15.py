class Solution(object):
    def threeSum(self, nums):
        if len(nums) <= 2:
            return []
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        res = []
        if 0 in hashmap and hashmap[0] >= 3: res.append([0,0,0])
        keyList = list(hashmap.keys())
        key_index = dict(zip(keyList, range(len(keyList))))
        for i in range(len(keyList)):
            for j in range(i+1, len(keyList)):
                num1 = keyList[i]
                num2 = keyList[j]
                value = - num2 - num1
                if value in hashmap:
                    if value != num1 and value != num2 and key_index[value] < j: continue  # 去重
                    if value == num1 and hashmap[num1] < 2: continue
                    if value == num2 and hashmap[num2] < 2: continue
                    res.append([value, num1, num2])
        return res
'''
两种不同的去重方式：
用顺序去重 
或者根据等于0的性质 分成正负哈希表去重
'''
a = Solution()
nums = [1,1,-2]
print(a.threeSum(nums))

'''
three sum题也可以用哈希表模仿 two sum 解法来做
哈希表解法： 主要是求多少个，比较难去重
双指针解法: 主要是求具体的数组， 比较容易去重
'''