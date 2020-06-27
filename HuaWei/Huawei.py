'''a,b =input('输入a,b空格隔开:').split()
#此时a,b为str型
a,b =map(int,input('输入a,b空格隔开:').split())
#此时a,b为int型'''
'''
python 常用 
字典： dic
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
字符串str转换成int: int_value = int(str_value)
int转换成字符串str: str_value = str(int_value)
去除 空格 
s.replace(' ')
l.sort()
k = sorted()
def takeSecond(elem):
    return elem[1] 
# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# 指定第二个元素排序
random.sort(key=takeSecond)
# 按value 排序
[ v for v in sorted(di.values())] 

'''

'''
import heapq

#1 heappush生成堆+ heappop把堆从小到大pop出来
heap = []
data = [1,3,5,7,9,2,4,6,8,0]
for i in data:
    heapq.heappush(heap,i)
print(heap)

lis = []
while heap:
    lis.append(heapq.heappop(heap))
print(lis)

#2 heapify生成堆+ heappop把堆从小到大pop出来
data2 = [1,5,3,2,9,5]
heapq.heapify(data2)
print(data2)

lis2 = []
while data2:
    lis2.append(heapq.heappop(data2))
print(lis2)
'''

'''
while True:
    try:
        s = input()
        dic = '123456789ABCDEF'
        s = s[2:]
        res = 0
        base = 0;
        for i in range(len(s)):
            base = 16 ** (len(s) - i - 1)
            for j in range(len(dic)):
                if s[i] == dic[j]:
                    res += base * (j + 1)
        print(res)
    except:
        break

'''

'''
map 方法的用法：
print(" ".join(map(str, res)) + " " if res else str(a) + " ")
map(fun, list) : map(int,'123'/(1,2,3)/{1:2,2:3,3:4}) = [1,2,3]
'''

'''
s1 = list(set(s))
s1.sort(key=s.index)
用map若要返回list 需要 list(map())
'''

'''
num=int(input())
dict={}
for i in range(num):
    m, n = map(int, input().split())
    if dict. __contains__(m):
        dict[m]+=n
    else:
        dict[m]=n
dic= sorted(dict.keys())
for i in dic:
    print(i,dict[i])
    
dic.has_key(key)
dic.pop(key)
dic.popitem  

#还是一行搞定： 
[ v for v in sorted(di.values())] 

#用lambda表达式来排序，更灵活： 
sorted(d.items(), lambda x, y: cmp(x[1], y[1])), 或反序： 
sorted(d.items(), lambda x, y: cmp(x[1], y[1]), reverse=True) 

#用sorted函数的key参数（func）排序： # 按照value进行排序 
print sorted(dict1.items(), key=lambda d: d[1]) 


>>> student_tuples = [
...     ('john', 'A', 15),
...     ('jane', 'B', 12),
...     ('dave', 'B', 10),
... ]
>>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
    '''

'''
from collections import defaultdict
while True:
    try:
 
        a,dd=int(input()),defaultdict(int)
        for i in range(a):
            key,val=map(int,input().split())
            dd[key]+=val
        for i in sorted(dd.keys()):
            print(str(i)+" "+str(dd[i]))
 
 
    except:
        break
'''

'''
def findStr(index,l, r, s):
    index = index
    maxLen = 0
    resStr = ''
    while (index < len(s) - 1 and index+r<len(s)):
        left = l
        right = r
        if s[index + left] == s[index + right]:
            while left + index > 0 and right + index < len(s) - 1:
                if s[index + left - 1] == s[index + right + 1]:
                    left = left - 1
                    right = right + 1
                else:
                    break
            if maxLen < (right + 1 - left):
                maxLen = right + 1 - left
                resStr = s[index + left:index + right + 1]
        if (index + right + 1 == len(s)):
            break
        index += 1
    return resStr
s = input()
if len(s) == 0 or len(s) == 1:
    print(s)
if len(list(set(s)))== 1:
    print(s)
else:
    index =0
    maxLen = 0
    resStr1 = findStr(index,0,1,s)
    resStr2 = findStr(index,0,2,s)
    if len(resStr1) > len(resStr2):
        print(resStr1)
    else:
        print(resStr2)
'''

'''stack = []
i = 0
s = s.replace(' ','')
while(i<len(s)):
    if s[i] == "*":
        i += 1
        v1 = stack.pop()
        v1 = int(v1)
        stack.append(v1 * int(s[i]))
        i += 1
    elif s[i] == "/":
        i += 1
        v1 = stack.pop()
        v1 = int(v1)
        stack.append(v1 / int(s[i]))
        i += 1
    else:
        start = i
        while(s[i].isdigit() and i+1<len(s) and s[i+1].isdigit()):
            i += 1
        i += 1
        stack.append(s[start:i])
res = int(stack[0])
i = 1
while i < len(stack):
    start = i
    if stack[i] == "+":
        i += 1
        res += int(stack[i])
        i += 1
    elif stack[i] == "-":
        i += 1
        res -= int(stack[i])
        i += 1


print(res)'''

'''自己写的方法
stack = []
index = []
start = []
if(len(n) == 0 or len(n) == 1):
    print(0)
for i in range(len(n)):
    if len(stack) == 0:
        stack.append(n[i])
        if n[i] == "(":
            start.append(i)
    else:
        if n[i] == "(":
            stack.append(n[i])
            start.append(i)
        elif n[i] == ")" and stack[-1] == "(":
            stack.pop()
            index.append(i)
            index.append(start.pop())
        else:
            stack.append(n[i])
index.sort()
maxLen = 0
curLen = 1
for i in range(len(index)-1):
    if index[i] == index[i+1] -1:
        curLen += 1
    else:
        if curLen>maxLen:
            maxLen = curLen
        curLen = 1
if curLen>maxLen and curLen >1 :
    maxLen = curLen
print(maxLen)
'''
'''
index = []
b = [0]*len(s)
for i in range(len(s)):
    if s[i] == '(':
        index.append(i)
    elif len(index)>0:
        b[index.pop()] = 1
        b[i] = 1
maxLen = 0
curLen =0
for i in b:
    if i:
        curLen += 1
    else:
        maxLen = max(maxLen, curLen)
        curLen =0
print(max(maxLen, curLen))
'''

'''
别人的解法：使用Collections中的Counter构造hashmap
class Solution(object):
    def findSubstring(self, s, words):
        from collections import Counter
        if not s or not words:
            return []

        words_len = len(words[0])           # 一个单词的长度
        words_num = len(words)              # words中单词的个数
        words_cnt = Counter(words)          # {'foo': 1, 'bar': 1}
        s_len = len(s)                      # 字符串s的长度
        res = []                            # 存储起始位置

        W = words_len * words_num           # 此处窗口大小为 2*3
        left = 0
        while (left + W) <= s_len:
            tmp = []
            i = left
            for j in range(words_num):       # 将窗口内的字符串添加到tmp中
                tmp.append(s[i:i + words_len])
                i = i + words_len
            tmp = Counter(tmp)
            if tmp == words_cnt:
                res.append(left)
                left = left + 1
            else:
                left = left + 1
        return res
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import Counter
        if len(s)==0 or len(words)== 0:
            return []
        words_num = len(words)
        words_len = len(words[0])
        res =[]
        wordsDic = Counter(words)
        for i in range(len(s)-words_num*words_len+1):
            strTemp = []
            for j in range(words_num):
                strTemp.append(s[j*words_num+i: j*words_num+words_len])
            if Counter(strTemp) == wordsDic:
                res.append(i)
        return res



'''

'''
import collections
import heapq
class Solution:
    # Time Complexity = O(n + nlogk)
    # Space Complexity = O(n)
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = []
        for key, value in count.items():
            heapq.heappush(heap, Word(value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap).word)
        return res[::-1]

class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    
    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.word
'''
'''华为机试第一题'''
'''
def dfs(graph, stack, destination, hasLoop, visited):
    if(len(stack) == 0):
        return False
    else:
        v = stack[-1]
        temp = graph[v]
        while temp.next is not None:
            if v==destination:
                visited = [0]*10
                visited[v] = 1
            if temp.next.data == destination:
                hasLoop[destination] = 1
                print(stack)
            else:
                if visited[temp.next.data] == 0 and temp.next.data>destination:
                    visited[temp.next.data] = 1
                    stack.append(temp.next.data)
                    dfs(graph, stack, destination,hasLoop,visited)
            temp = temp.next
        stack.pop()

s = input().split(']') #1:[2,3],4:[1],3:[4],2:[4]
wholePaths = []
s = s[0:len(s)-1]
if len(s) == 1:
    print("OK")
else:
    graph = []
    count_in = [0]*10
    vector = []
    checkVector =[]
    stack = []
    hasLoop = [0]*10
    visited = [0]*10
    for i in range(10):
        graph.append(Node(i))
    #图的邻接链表
    for i in range(len(s)):
        if i == 0:
            id = int(s[i][0])
        else:
            id = int(s[i][1])
        vector.append(id)
        for j in range(3,len(s[i])):
            if s[i][j].isdigit():
                count_in[int(s[i][j])] += 1
                if(graph[id].next is not None):
                    tempNode.next = Node(int(s[i][j]))
                    tempNode = tempNode.next
                else:
                    tempNode = Node(int(s[i][j]))
                    graph[id].next = tempNode
    vector = sorted(vector)
    for i in vector:
        if count_in[i] > 0 :
            checkVector.append(i)
    if len(checkVector) == 0:
        print("OK")
    for i in checkVector:
        stack.append(i)
        dfs(graph, stack, i, hasLoop, visited)
    if sum(hasLoop) == 0:
        print("OK")'''



'''
abc
def
==
aga'-=
123
123
abc
  
'''
def is_valid(key):
    if (key>='0'and key<='9') or (key>='a'and key<='z') or (key>='A' and key<='Z'):
        return True
    return False

n = 100
s =[]
valid_str = []
invalid_str = []
bool_valid =True
while n>0:
    a = input()
    if a[0] == ' ':
        break
    s.append(a)
    n -= 1
if len(s) == 0:
    print("")
    print("")
else:
    for word in s:
        bool_valid = True
        for j in range(len(word)):
            if not is_valid(word[j]):
                invalid_str.append(word)
                bool_valid = False
                break
        if bool_valid:
            valid_str.append(word)
    dic = list(set(valid_str))
    dic.sort(key=valid_str.index)
    print(' '.join(dic))
    print(' '.join(invalid_str))



































