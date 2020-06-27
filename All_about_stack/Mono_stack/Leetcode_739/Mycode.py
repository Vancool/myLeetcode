class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if len(T) == 0:
            return []
        if len(T) == 1:
            return [0]
        Tstack = []
        res = [0]*len(T)

        for i in range(len(T)-1,-1,-1):
            if len(Tstack) == 0:
                Tstack.append(T[i])
                res[i] = 0
            elif Tstack[-1] > T[i]:
                Tstack.append(T[i])
                res[i] = 1
            else:
                temp = i+1
                while len(Tstack)>0 and T[i] >= Tstack[-1]:
                    if res[temp] == 0:
                        Tstack.pop()
                        res[i] = 0
                        Tstack.append(T[i])
                        break
                    else:
                        Tstack.pop()
                        res[i] += res[temp]
                        temp = temp + res[temp]
                if T[i] < Tstack[-1]:
                    res[i] += 1
                    Tstack.append(T[i])

        return res

if __name__ =="__main__":
    a = Solution()
    print(a.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))


