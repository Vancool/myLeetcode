class Solution(object):
    def numberToWords(self, num):
        if num == 0: return "Zero"
        low_digit = {0:"",1:"One",2:"Two",3:"Three",4: "Four",5:"Five",6:"Six",
                 7:"Seven",8:"Eight",9:"Nine"}
        middle_digit = {0:"",10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14: "Fourteen",15:"Fifteen",16:"Sixteen",
                 17:"Seventeen",18:"Eighteen",19:"Nineteen",20:"Twenty",30:"Thirty",40: "Forty",50:"Fifty",60:"Sixty",
                 70:"Seventy",80:"Eighty",90:"Ninety"}
        high_val = [ "Thousand","Million", "Billion"]
        low = 0
        high = 0
        res = []
        flag = False
        while num:
            if not low:
                key = int(num % 100)
                if not key:
                    num = num // 100
                    low += 2
                    flag = True
                else:
                    if key in middle_digit:
                        num = num // 100
                        res.append(middle_digit[key])
                        low += 2
                        flag = True
                    elif key in low_digit:
                        num = num //100
                        # if num:
                        #     res = "And "+low_digit[key]+" "+res
                        # else:
                        res.append(low_digit[key])
                        low += 2
                        flag = True
            if not flag:
                num, key = divmod(num, 10)
                if key:
                    if low == 0:
                        res.append(low_digit[key])
                        # res = low_digit[key] + " " + low_val[low] + res
                    if low == 1:
                        res.append(middle_digit[key*10])
                        # res = middle_digit[key*10] + " " + low_val[low]+res
                    if low == 2:
                        res.append("Hundred")
                        res.append(low_digit[key])
                        # res =  + " " + low_val[low]+" " + res
                low += 1
            if not num: break
            if low > 2:
                low = int(low % 3)
                while len(res) > 0 and res[-1] in high_val:
                    res.pop()
                res.append(high_val[high])
               # res = high_val[high] +" " + res
                high = int((high+1)%3)
            flag = False
        return " ".join(res[::-1])


a = Solution()
key = 123
print(a.numberToWords(key))