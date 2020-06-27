class Solution(object):
    def minDistance(self, word1, word2):
        self.res = float('inf')

        memohash = {}
        def Process(num1, num2, index1, index2, count):
            if (index1, index2) in memohash:
                return memohash[(index1, index2)]
            if index1 == len(word1) or index2 == len(word2):
                if num1 >= num2:
                    self.res = min(num1-num2+count, self.res)
                else:
                    self.res = min(num2-num1+count, self.res)
            elif word1[index1] == word2[index2]:
                Process(num1, num2, index1+1, index2+1, count)
            else:
                w1 = word1[index1]
                w2 = word2[index2]

                Process(num1, num2, index1 + 1, index2 + 1, count+1) # 替换
                Process(num1 - 1, num2, index1 + 1, index2, count + 1)  # 删除
                Process(num1 + 1, num2, index1, index2 + 1, count + 1)  # 增加
            memohash[(index1, index2)] = self.res

        Process(len(word1), len(word2), 0,0,0)
        return self.res
'''
编辑距离： https://leetcode-cn.com/problems/edit-distance/solution/bian-ji-ju-chi-mian-shi-ti-xiang-jie-by-labuladong/
其实自己大框架已经做出来了，只是有些地方没想对，比如当到达边界条件的时候我应该怎么处理
test case:
w1 = "sea"
w2 = "eat"
'''
a = Solution()
w1 = "sea"
w2 = "eat"
print(a.minDistance(w1, w2))
print("Done")