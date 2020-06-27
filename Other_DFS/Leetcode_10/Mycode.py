from collections import deque
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == None or p == None:
            return False
        if len(s) == 0:
            return len(p) == 0 or (len(p) == 2 and p[-1]=='*')
        if len(p) == 0:
            return False
        n = len(s)
        m = len(p)
        i = 0
        j = 0
        stack = deque()
        while i < n and j < m:
            if s[i] == p[j] or p[j] == '.':
                stack.append(p[j])
                i += 1
                j += 1
            else:
                if p[j] == '*':
                    if s[i] == stack[-1] or stack[-1] == '.':
                        i += 1
                    elif j+1<m and (p[j+1] == s[i] or p[j+1] == '.'):
                        stack.append(p[j+1])
                        j = j+2
                        i = i+1
                    else:
                        return False
                else:
                    if j+1 == m or p[j+1] != '*' :
                        return False
                    else:
                        j += 2
        if i == n and (j == m or (j==m-1 and p[-1] == '*')):
            return True
        else:
            return False



class Solution2(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == None or p == None:
            return False
        if len(s) == 0:
            return len(p) == 0 or (len(p) == 2 and p[-1]=='*')
        if len(p) == 0:
            return False
        n = len(s)
        m = len(p)
        i = n-1
        j = m-1
        while i >-1 and j >-1:
            if s[i] == p[j] or p[j] == '.':
                i -= 1
                j -= 1
            else:
                if p[j] == '*':
                    if j-1 >= 0:
                        if p[j-1] == '.' or p[j-1]==s[i]:
                            i -= 1
                        else:
                            j = j-2
                    else:
                        return False
                else:
                    return False
        while j>=0 and p[j] == '*':
            j -= 2
        if i >= 0 or j>= 0:
            return False
        return True

class Solution3(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            return len(s) == 0
        if s == None or p == None:
            return False
        if len(p) == 1:
            if len(s) == 1:
                return p[0] == s[0] or p[0] == '.'
            else:
                return False
        n = len(s)
        m = len(p)
        i = n-1
        j = m-1
        while i >= 0 and j>= 0 and (s[i] == p[j] or p[j] == '.'):
            i -= 1
            j -= 1
        if i<0 and j<0:
            return True
        if p[j] == '*':
            if len(p) == 2 and len(s) == 0:
                return True
            if i<0:
                return self.isMatch('', p[0:j-1])
            if s[i] != p[j-1] and p[j-1]!='.':
                return self.isMatch(s[0:i+1], p[0:j-1])
            else:
                if p[j-1] == '.' or (i-1 >= 0 and s[i-1] == s[i]):
                    return self.isMatch(s[0:i],p[0:j-1]) or self.isMatch(s[0:i],p[0:j+1]) or self.isMatch(s[0:i+1],p[0:j-1])
                else:
                    return self.isMatch(s[0:i], p[0:j-1]) or self.isMatch(s[0:i+1],p[0:j-1])
        else:
            return False


class Solution4(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            return len(s) == 0
        if len(p) == 1:
            if len(s) == 1:
                return p[0] == s[0] or p[0] == '.'
            else:
                return False
        i = len(s)-1
        j = len(p)-1
        if p[j] == '*':
            if i < 0:
                return self.isMatch('',p[0:j - 1])
            if p[j - 1] != '.' and p[j - 1] != s[i]:
                return self.isMatch(s[0:i + 1], p[0:j - 1])
            else:
                return self.isMatch(s[0:i + 1], p[0:j - 1]) or self.isMatch(s[0:i], p[0:j - 1]) or self.isMatch(s[0:i],
                                                                                                              p[
                                                                                                                0:j + 1])
        if j>=0 and i>=0 and (p[j] == '.' or p[j] == s[i]):
            return self.isMatch(s[0:i], p[0:j])
        return False

a =Solution4()
s = "mississippi"
p = "mis*is*ip*."
print(a.isMatch(s,p))
print("Done")


