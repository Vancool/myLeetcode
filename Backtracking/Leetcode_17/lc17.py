class Solution(object):
    def letterCombinations(self, digits):
        dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        def Process(pre, start, digit):
            if start >= len(digit):
                return
            if start == len(digit)-1:
                key = dic[digit[start]]
                for k in key:
                    pre.append(k)
                    res.append(''.join(pre))
                    pre.pop()
                return
            key = dic[digit[start]]
            for k in key:
                pre.append(k)
                Process(pre, start+1, digit)
                pre.pop()
        Process([], 0, digits)
        return res

if __name__ == "__main__":
    a = Solution()
    digit = ""
    print(a.letterCombinations(digit))
    print("Done")


