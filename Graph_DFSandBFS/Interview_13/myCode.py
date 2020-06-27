class Solution1(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 1
        def validStep(i,j, k):

            return (i % 10 + i // 10 + j % 10 + j // 10 <= k)

        #direction = [(1,0),(-1,0),(0,1),(0,-1)]
        count = 1
        graph = [[0]*n for _ in range(m)]
        graph[0][0] = 1
        for i in range(m):
            if not validStep(i,0,k):
                break
            for j in range(n):
                #print(i,j)
                if validStep(i, j, k) and (\
                        (i-1>=0and graph[i-1][j]==1)or \
                        (j-1>=0 and graph[i][j-1]==1 or\
                        (i+1<m and graph[i+1][j]==1 )or\
                        (j+1<n and graph[i][j+1] == 1 ))):
                    count += 1
                    graph[i][j] = 1
                elif i!=0 and j!=0:
                    if n<=10:
                        break
                    if n >10 and validStep(i,10,k) and graph[i][j] == 0:
                        j = 10
        print(graph)
        return count



class Solution2(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 1
        def validStep(x,y, key):
            val = 0
            while x:
                val += x%10
                x = x //10
            while y:
                val += y%10
                y = y // 10
            return val <= key

        #direction = [(1,0),(-1,0),(0,1),(0,-1)]
        count = 0
        graph = [[0]*n for _ in range(m)]
        graph[0][0] = 1
        for i in range(m):
            for j in range(n):

                if validStep(i, j, k) and (\
                        (i-1>=0and graph[i-1][j]==1)or \
                        (j-1>=0 and graph[i][j-1]==1 or\
                        (i+1<m and graph[i+1][j]==1 )or\
                        (j+1<n and graph[i][j+1] == 1 ))):
                    count += 1
                    graph[i][j] = 1
                else:
                    break
        print(graph)
        return count
a = Solution1()
print('A')
print(a.movingCount(1,2,1))
# b = Solution2()
# print('B')
# print(b.movingCount(38,15,9))
print("Done")
