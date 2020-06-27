


T = list(map(int,input().split(',')))

'''
很好的写法： 如果求元素相隔的距离其实容器里面放下标会更好
stack里面可以存下标，然后算两个元素差多少的时候可以用下标来相减计算
正序可以算，反序也可以算
'''
'''
方法一：正序，如果往前走的时候没找到比它大的，我先存着下标然后一个一个弹出来比较
得到一个递减栈
'''
indexStack =[]
res = [0]*len(T)
for i in range(len(T)):
    while len(indexStack)>0 and T[i] > T[indexStack[-1]]:
            topIndex = indexStack.pop()
            res[topIndex] = i-topIndex
    indexStack.append(i)
print(res)

'''
方法二，反序操作
'''

indexStack =[]
res = [0]*len(T)
for i in range(len(T)-1,-1,-1):
    while len(indexStack)>0 and T[i] >= T[indexStack[-1]]:
        indexStack.pop()
    if len(indexStack)>0:
        res[i] = indexStack[-1]-i
    indexStack.append(i)
print(res)