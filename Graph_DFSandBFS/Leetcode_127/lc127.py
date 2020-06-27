from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not wordList or endWord not in wordList:
            return 0
        def isValid(word1, word2):
            if len(word1) != len(word2): return False
            count = 1
            for i in range(len(word2)):
                w1 = word1[i]
                w2 = word2[i]
                if w1 != w2:
                    if not count: return False
                    count -= 1
            return True
        visited = set()
        queue = deque()
        queue.append(beginWord)
        count = 0
        while queue:
            count += 1
            for _ in range(len(queue)):
                out = queue.popleft()
                if out == endWord: return count
                for word in wordList:
                    if word not in visited and isValid(out, word):
                        visited.add(word)
                        queue.append(word)
        return 0

'''
我自己写的bfs 
解法思路没问题，但是超时了
优化方法： 1.把哈希表改成bool值可以省去哈希计算和查找的时间
          2.要在碰到目标点的时候直接返回，而不是要入队出队遍历完了再返回
          3.可以考虑双端BFS从出发和目标一起同时搜索
          4.考虑双端BFS每次选择queue中包含节点最少的那个点做BFS步骤
          
        对于判断str 和 str 差一个：
        1. str 和 str 直接比 O（N^2） N为 str的数量
        2. str遍历每个字符看是否符合另一个str 用哈希表， 时间复杂度O(N*M) 
        M为字符长度，但是要耗费空间存哈希表
'''

'''
优化的普通BFS方法
'''

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if not wordList or endWord not in wordList or not beginWord or not endWord:
            return 0
        def isValid(word1, word2):
            count = 1
            for i in range(len(word2)):
                w1 = word1[i]
                w2 = word2[i]
                if w1 != w2:
                    if not count: return False
                    count -= 1
            return True
        visited = [False] * len(wordList)
        queue = deque()
        queue.append(beginWord)
        count = 0
        while queue:
            count += 1
            for _ in range(len(queue)):
                out = queue.popleft()
                for i in range(len(wordList)):
                    word = wordList[i]
                    if not visited[i] and isValid(out, word):
                        if word == endWord: return count + 1
                        visited[i] = True
                        queue.append(word)
        return 0

'''
还是超时了，尴尬
双向BFS解法,如果两边同时出现同一个数即可达
'''
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if not wordList or endWord not in wordList or not beginWord or not endWord:
            return 0
        def isValid(word1, word2):
            count = 1
            for i in range(len(word2)):
                w1 = word1[i]
                w2 = word2[i]
                if w1 != w2:
                    if not count: return False
                    count -= 1
            return True
        visited1 = set()
        visited2 = set()
        q1 = deque()
        q1.append(beginWord)
        visited1.add(beginWord)
        q2 = deque()
        q2.append(endWord)
        visited2.add(endWord)
        count = 0
        while q1 and q2:
            if len(q1) > len(q2):
                tmp = q1
                q1 = q2
                q2 = tmp
                tmp = visited1
                visited1 = visited2
                visited2 = tmp
            count += 1
            for i in range(len(q1)):
                out = q1.popleft()
                for word in wordList:
                    if word not in visited1 and isValid(out, word):
                        if word in visited2:
                            return count + 1
                        visited1.add(word)
                        q1.append(word)
        return 0

'''
换成另一种判断字符串的方法
'''

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if not wordList or endWord not in wordList or not beginWord or not endWord:
            return 0
        wordList = set(wordList)
        visited1 = set()
        visited2 = set()
        q1 = deque()
        q1.append(beginWord)
        visited1.add(beginWord)
        q2 = deque()
        q2.append(endWord)
        visited2.add(endWord)
        count = 0
        while q1 and q2:
            if len(q1) > len(q2):
                tmp = q1
                q1 = q2
                q2 = tmp
                tmp = visited1
                visited1 = visited2
                visited2 = tmp
            count += 1
            for i in range(len(q1)):
                tmp = q1.popleft()
                tmp = list(tmp)
                for i in range(len(tmp)):
                    ch = tmp[i]
                    for key in range(ord('a')+26):
                        tmp[i] = chr(key)
                        word = "".join(tmp)
                        if word in visited2: return count + 1
                        if word in wordList and word not in visited1:
                            if word in visited2: return count + 1
                            visited1.add(word)
                            q1.append(word)
                    tmp[i] = ch
        return 0

'''
超简洁代码：
'''
import string


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordDict, step = set(wordList), 1
        if endWord not in wordDict:
            return 0
        # set的查询速度快
        s1, s2 = set([beginWord]), set([endWord])
        while s1:
            stack = set([])
            wordDict -= s1 # 集合差
            for s in s1:
                for i in range(len(beginWord)):
                    for j in string.ascii_lowercase:
                        tmp = s[:i] + j + s[i + 1:]
                        if tmp not in wordDict:
                            continue
                        if tmp in s2:
                            return step + 1
                        stack.add(tmp)
            if len(stack) < len(s2):
                s1 = stack
            else:
                s1, s2 = s2, stack
            step += 1
        return 0
a = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(a.ladderLength(beginWord, endWord, wordList))



