import random
'''
不明白为什么用了随机就是不行emmmm
'''
class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0 or len(arr) == 0:
            return []
        def partition(num, left, right):
            if right == left:
                return right
            index = random.randint(left, right)
            num[left], num[index] = num[index], num[left]
            pivot = num[left]
            l = left + 1
            r = right
            while l <= r:
                while l <= r and  num[l] < pivot:
                    l += 1
                while l <= r and num[r] > pivot:
                    r -= 1
                if l >= r:
                    break
                num[l], num[r] = num[r], num[l]
                l += 1
                r -= 1
            num[r], num[left] = num[left], num[r]
            return r
        def quickSearch(num, left, right, k):
            #这个函数是找下标为k的元素
            index = partition(num, left, right)
            if index == k:
                return list(num[0:k+1])
            elif index > k:
                return quickSearch(num, left, index-1, k)
            else:
                return quickSearch(num, index+1, right, k)
        return quickSearch(arr, 0, len(arr)-1, k-1)

a = Solution()
arr = [0,0,1,2,4,2,2,3,1,4]
print(a.getLeastNumbers(arr, 8))
print("Done")
