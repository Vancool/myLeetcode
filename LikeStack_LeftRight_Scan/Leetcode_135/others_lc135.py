class Solution1(object):
    def candy(self, ratings):
        if len(ratings) == 0 or len(ratings) == 1:
            return len(ratings)
        candycount = [1] * len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i-1] < ratings[i]:
                candycount[i] = candycount[i-1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candycount[i] = max(candycount[i], candycount[i+1]+1)
        return sum(candycount)



'''
解法一：
因为要统计左右两边然后选择栈尾要是什么数值,而不是维护一个单调栈一碰到不同的就开始统计弹出
因此只能从左到右统计递增 从右到左统计递减 然后最后取一个最优解


解法二.
可以实际地统计一下，然后计算一个顶峰的值左右两边
个人觉得他的题解不错：
https://leetcode-cn.com/problems/candy/solution/fen-fa-tang-guo-by-powcai/
'''
class Solution(object):
    def candy(self, ratings):
        if len(ratings) == 0 or len(ratings) == 1:
            return len(ratings)
        ratings.append(1<<31-1) #哨兵
        pre = 1
        res = 1
        down = 0
        for i in range(1,len(ratings)):
            if ratings[i] >= ratings[i-1] and down == 0:
                #在上坡或者平坡
                if ratings[i] == ratings[i - 1]:
                    pre = 1
                elif ratings[i] > ratings[i - 1]:
                    pre += 1
                res += pre
            elif ratings[i] >=  ratings[i-1] and down > 0:
                #上坡刚开始, 用等差数列求和把下坡全部加起来
                res += (down + 1)* down // 2
                if down >= pre:
                    #说明在上一个山中右边下坡的节点比左边上坡的节点多,要把之前没算的顶部算上
                    res += down - pre + 1
                down = 0
                '''注意这边如果down已经算完了就要置为0'''
                if ratings[i] == ratings[i-1]:
                    pre = 1
                elif ratings[i] > ratings[i-1]:
                    pre = 2
                res += pre
            else:
                # 下坡
                down += 1
        return res - pre

a = Solution()
r = [1,0,2]
print(a.candy(r))
print("Done")




