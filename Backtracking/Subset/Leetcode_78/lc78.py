class Solution(object):
    def subsets(self, nums):
        if len(nums) == 0: return [[]]
        self.res = []
        #nums.sort() 没有重复不需要
        def recur(index, path):
            self.res.append(path)
            for i in range(index, len(nums)):
                recur(i+1, path + [nums[i]])

        recur(0,[])
        return self.res
'''
我自己写的是广度优先遍历的方法， 选一个，选两个，选三个
广度优先另一种思路， 迭代写法
只要记得保持index顺序， 顺序数组在外层就好
否则就变成了组合了
这样的话得到的最终是一个n叉树

空间和时间复杂度 O（n * 2^n） 
子节点和复制每个数组用的时间
'''
class Solution(object):
    def subsets(self, nums):
        res = [[]]
        for n in nums:
            for i in range(len(res)): #不能用迭代器
                ans = res[i] + [n]
                res += [ans]
        return res


'''
另一种想法：
选与不选，这样就变成了深度优先的二叉树
两种编码方式：  递归 / 二进制编码01作为选与不选
'''
class Solution(object):
    def subsets(self, nums):
        if len(nums) == 0: return [[]]
        self.res = []
        def process(index, path):
            if index == len(nums):
                self.res.append(path)
                return
            process(index+1, path)
            process(index+1, path + [nums[index]])
        process(0,[])
        return self.res



class Solution(object):
    def subsets(self, nums):
        if len(nums) == 0: return [[]]
        all_subset_num = 1<<len(nums)
        res = []
        for i in range(all_subset_num):
            subset = []
            for j in range(all_subset_num):
                if (i >> j) & 1:
                    subset.append(nums[j])
            res.append(subset)
        return res



a = Solution()
nums = [1,2,3]
print(a.subsets(nums))
