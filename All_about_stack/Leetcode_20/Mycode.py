class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s)&1 == 1:
            return False
        stack =[]
        dict = {'(':')', '{':'}','[':']'}
        for ch in s:
            if ch not in dict.keys() and len(stack) == 0:
                return False
            elif ch in dict.keys():
                stack.append(ch)
            else:
                if ch == dict[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

if __name__ == "__main__":
    a =Solution()
    print(a.isValid("()[]{}"))
