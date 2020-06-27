class Solution(object):
    def generateParenthesis(self, n):
        if n == 0: return []
        res = []
        def dfs(leftnum, rightnum, path, n):
            if leftnum == rightnum == n:
                res.append(path)
                return
            if leftnum < n:
                dfs(leftnum+1, rightnum, path+"(", n)
            if rightnum < n and rightnum < leftnum:
                dfs(leftnum, rightnum+1, path + ")", n)

        dfs(0,0,"", n)
        return res
'''
回溯法
用左括号和右括号的数量剪枝
当前无效的括号是 右括号比左括号数量多的，因此只有 left >= right时候才会继续往下回溯
'''
a = Solution()
print(a.generateParenthesis(3))
print("Done")