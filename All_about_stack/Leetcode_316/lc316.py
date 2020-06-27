class Solution(object):
    def removeDuplicateLetters(self, s):
        in_stack = [False] * 26
        freq = [0] * 26
        stack = []
        for key in s:
            index = ord(key) - ord("a")
            freq[index] += 1
        for key in s:
            if in_stack[ord(key)-ord('a')]:
                freq[ord(key) - ord('a')] -= 1
                continue
            while len(stack) > 0 and stack[-1] > key and freq[ord(stack[-1]) - ord('a')] > 0:
                tmp = stack.pop()
                in_stack[ord(tmp)-ord('a')] = False
            in_stack[ord(key) - ord('a')] = True
            stack.append(key)
            freq[ord(key) - ord('a')] -= 1
        return "".join(stack)
'''
用栈来解， 真的好题， 神奇
'''

a = Solution()
print(a.removeDuplicateLetters("bbcaac"))
print("Done")