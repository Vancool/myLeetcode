from collections import defaultdict
'''
记忆递归
'''
class Solution(object):
    def wordBreak(self, s, wordDict):
        dict = set(wordDict)
        memomap = defaultdict(list)

        def Process(start):
            if start >= len(s):
                return []
            if start in memomap:
                return memomap[start]
            if s[start:len(s)] in dict:
                memomap[start].append(s[start:len(s)])
            for i in range(start + 1, len(s) + 1):
                if s[start:i] in dict:
                    backstr = Process(i)
                    if len(backstr) > 0:
                        for st in backstr:
                            memomap[start].append(s[start:i] + st)
            return memomap[start]

        return Process(0)


