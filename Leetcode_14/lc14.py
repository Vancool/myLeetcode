class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        tmp = strs[0]
        res = []
        for i in range(len(tmp)):
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or strs[j][i] != tmp[i]:
                    return ''.join(res)
            res.append(tmp[i])
        return "".join(res)