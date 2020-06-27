class Solution(object):
    def simplifyPath(self, path):
        path = path.split("/")
        stack = []
        res = "/"
        for p in path:
            if not p or p == '.': continue
            if p == ".." and stack:
                stack.pop()
            if p != "..":
                stack.append(p)
        # if stack:
        #     stack = "/".join(stack)
        #     res += stack
        # 可以写成底下这样
        res += "/".join(stack)
        return res


a = Solution()
path = "/a/../../b/../c//.//"
print(a.simplifyPath(path))
k = []
print('/'.join(k))
print("Done")