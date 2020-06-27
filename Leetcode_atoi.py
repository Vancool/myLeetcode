class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str == None:
            return 0
        str = str.lstrip()
        if len(str) == 0:
            return 0
        if (not(str[0] == '-' or str[0] == '+' or str[0].isdigit())):
            return 0
        INI_MIN = -2**31
        INI_MAX = 2**31 - 1
        i = 1
        while(i < len(str)):
            if(str[i].isdigit()):
                i += 1
            else:
                break
        str = str[0:i]
        if str == '-':
            return 0
        elif str == '+':
            return 0
        else:
            if(str[0] == '-'):
                a = -int(str[1:i])
            elif(str[0] == '+'):
                a = int(str[1:i])
            else:
                a = int(str)
            if a < INI_MIN:
                return INI_MIN
            if a > INI_MAX:
                return INI_MAX
            else:
                return a

if __name__ == "__main__":
    b = Solution()
    print(b.myAtoi("+123 hahha"))