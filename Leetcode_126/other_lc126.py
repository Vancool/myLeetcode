from collections import deque
import string
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        if not beginWord or not endWord or not wordList: return []
        wordList = set(wordList)
        if endWord not in wordList: return []
        visited = set()
        visited.add(beginWord)
        res = []
        queue = deque()
        queue.append([beginWord])
        while queue:
            flag = False
            for _ in range(len(queue)):
                subvisited = set()
                out = queue.popleft()
                key = out[-1]
                for i in range(len(key)):
                    ch = key[i]
                    for j in string.ascii_lowercase:
                        if ch == j: continue
                        tmp = key[:i] + j + key[i+1:]
                        if tmp not in visited and tmp in wordList:
                            if tmp == endWord:
                                res.append(out + [tmp])
                                flag = True
                            else:
                                queue.append(out + [tmp])
                                subvisited.add(tmp)
            if flag: break
            visited |= subvisited
        return res
'''
超时 时间复杂度为 N * m * 26

同样的想法，如果先用 BFS构图会比隐式构图
'''
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        if not beginWord or not endWord or not wordList: return []
        wordList = set(wordList)
        if endWord not in wordList: return []
a = Solution()
begin = "red"
end = "tax"
l = ["ted","tex","red","tax","tad","den","rex","pee"]
print(a.findLadders(begin, end, l))



