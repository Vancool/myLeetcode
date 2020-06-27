class Solution(object):
    def scheduleCourse(self, courses):
        if len(courses) == 0: return 0
        self.res = 0
        taken = set()
        def recur(curTime, curNum, index, taken):
            if curTime + courses[index][0] > courses[index][1]:
                return
            curTime += courses[index][0]
            taken.add(index)
            curNum += 1
            self.res = max(self.res, curNum)
            for i in range(len(courses)):
                if i not in taken and curTime < courses[i][1]:
                    recur(curTime, curNum, i, taken)
            taken.remove(index)
        for i in range(len(courses)):
            recur(0,0,i,taken)
        return self.res
'''
超时
'''
a = Solution()
c = [[7,16],[2,3],[3,12],[3,14],[10,19],[10,16],[6,8],[6,11],[3,13],[6,16]]
print(a.scheduleCourse(c))
print("Done")

