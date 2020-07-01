class Trie:
    def __init__(self):
        self.root = {}
    def insert(self, word):
        root = self.root
        for w in word:
            if w not in root:
                root[w] = {}
            root  = root[w]
        root["end"] = root.get("end", 0) + 1

class Solution(object):
    def findWords(self, board, words):
        if not words: return words
        if not board or not board[0]: return []

        def dfs(trie_cur, x, y, path):
            if board[x][y] in trie_cur:
                path += board[x][y]
                if "end" in trie_cur[board[x][y]]:
                    self.res.append(path[:])
                tmp = board[x][y]
                board[x][y] = "#"
                for direct_x, direct_y in direction:
                    curx = x + direct_x
                    cury = y + direct_y
                    if 0 <= curx < len(board) and 0 <= cury < len(board[0]):
                        dfs(trie_cur[tmp], curx, cury, path)
                board[x][y] = tmp

        trie_root = Trie()
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        for word in words:
            trie_root.insert(word)
        m, n = len(board), len(board[0])
        self.res = []
        for i in range(m):
            for j in range(n):
                dfs(trie_root.root, i, j, "")
        return list(set(self.res))
'''
重复没有考虑

[["a","a"]]
["a"]
'''


a = Solution()
words = ["aaa"]
board =[["a","a"]]
print(a.findWords(board, words))





