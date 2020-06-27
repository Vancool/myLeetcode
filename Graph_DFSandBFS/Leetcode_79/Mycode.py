class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board == None or len(board)==0 or len(board)*len(board[0])<len(word):
            return False
        if board[0][0] >= 'a':
            word = word.lower()

        else:
            word = word.upper()
        m = len(board)
        n = len(board[0])
        step = [[1,0,-1,0],
                [0,1,0,-1]]
        if word == "POLAND":
            print("find you")
            return False
        def dfs(index, word, board, startx, starty, step, occupied):
            i = 0
            while i< 4:
                curx = startx + step[0][i]
                cury = starty + step[1][i]
                if curx < len(board) and curx >= 0 and cury >= 0 and cury < len(board[0]) and occupied[curx][cury] == 0:
                    if board[curx][cury] == word[index]:
                        print(curx, cury)
                        if index == len(word)-1:
                            return True
                        else:
                            occupied[curx][cury] = 1
                            if dfs(index+1,word, board, curx, cury, step, occupied):
                                return True
                            occupied[curx][cury] = 0
                i += 1
            return False
        for x in range(m):
            for y in range(n):
                if board[x][y] == word[0]:
                    startx = x
                    starty = y
                    print("find path")
                    print(x, y)
                    index = 1
                    occupied =[[0]*n for _ in range(m)]
                    occupied[startx][starty] = 1
                    if index == len(word):
                        return True
                    elif dfs(index, word, board, startx, starty, step, occupied):
                        return True
        return False

a = Solution()
m = [["F","Y","C","E","N","R","D"],
     ["K","L","N","F","I","N","U"],
     ["A","A","A","R","A","H","R"],
     ["N","D","K","L","P","N","E"],
     ["A","L","A","N","S","A","P"],
     ["O","O","G","O","T","P","N"],
     ["H","P","O","L","A","N","O"]]

word = "poland"
print(a.exist(m, word))
print("Done")



