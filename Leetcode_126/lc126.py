from collections import deque
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        if endWord not in wordList or not wordList or not beginWord:
            return []
        res = []
        visited1 = set([beginWord])
        visited2 = set([endWord])
        q1 = deque()
        q1.append(beginWord)
        q2 = deque()
        q2.append(endWord)
        min_count = float('inf')
        count = 0
        while q1 and q2:
            if len(q1) > len(q2):
                q1,q2 = q2,q1
                visited1, visited2 = visited2, visited1
            count += 1
            for _ in range(len(q1)):
                out = q1.popleft()
                for i in range(len(out)):
                    for j in range(len(ord('a')+26)):
                        tmp = out[:i] + chr(j) + out[i+1 :]
                        if tmp not in wordList or tmp in visited1: continue
                        if tmp in visited2:
                            min_count = min(count + 1, min_count)
                            if min_count == count + 1:
                                pass


'''
这一题我自己没写出来， 用的是BFS 和 DFS 的结合来做
单向BFS 或者 双端BFS
'''



