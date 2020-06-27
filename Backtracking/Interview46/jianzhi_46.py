class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        path = ''
        def Process(left, num, count, path):
            if left == len(num)-1:
                print(path+num[left])
                return count
            if len(num)-2 == left:
                if int(num[left:len(num)])<10 or 25 < int(num[left:len(num)]) < 100:
                    print(path + num[left:len(num)])
                    return count
                else:
                    print(path + num[left]+','+num[-1])
                    print(path + num[left:len(num)])
                    return count*2

            if 25 < int(num[left:left+2]) < 100 or int(num[left:left+2])<10:
                return Process(left+1, num, count, path+num[left]+',')
            else:
                return Process(left+1, num, count,path+num[left]+',') + Process(left+2, num, count, path+num[left:left+2]+',')
        res = Process(0, num, 1, path)
        return res

a = Solution()
num = 419605557
print(a.translateNum(num))
