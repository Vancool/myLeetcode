from queue import PriorityQueue
class Solution(object):
    def scheduleCourse(self, courses):
        if len(courses) == 0: return 0
        courses.sort(key=lambda x: x[1])
        Q = PriorityQueue()
        res = 0
        curTime = 0
        for i in range(len(courses)):
            if courses[i][0] + curTime <= courses[i][1]:
                res += 1
                Q.put(-courses[i][0])
                curTime += courses[i][0]
            else:
                if not Q.empty():
                    longTime = - Q.get()
                    curTime -= longTime
                    if longTime > courses[i][0] and curTime + courses[i][0] <=  courses[i][1]:
                        Q.put(-courses[i][0])
                        curTime += courses[i][0]
                    else:
                        Q.put(-longTime)
                        curTime += longTime
        return res

a = Solution()
c =  [[100,2],[32,50]]
print(a.scheduleCourse(c))
print("Done")
