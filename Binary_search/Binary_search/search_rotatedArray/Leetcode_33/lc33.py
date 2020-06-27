class Solution(object):
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        def bit_search(left, right, target):
            if left > right:
                return -1
            if left == right:
                return left if nums[left] == target else -1
            '''
            排除一下O（n）最差的可能, 排好了但是没找到就会一个一个找完
            '''
            if nums[left] < nums[right]:
                if nums[left] > target:
                    return -1
                if nums[right] < target:
                    return -1
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[left] < target:
                    return bit_search(left, mid-1, target)
                elif nums[left] > target:
                    if nums[right] < target:
                        return -1
                    elif nums[right] > target:
                        l = bit_search(left, mid-1, target)
                        r = bit_search(mid+1, right, target)
                        if l == -1 and r == -1:
                            return -1
                        else:
                            return r if  r!= -1 else l
                    else:
                        return right
                else:
                    return left
            elif nums[mid] < target:
                if nums[right] > target:
                    return bit_search(mid+1, right, target)
                elif nums[right] < target:
                    if nums[left] > target:
                        return -1
                    elif nums[left] < target:
                        l = bit_search(left, mid-1, target)
                        r = bit_search(mid+1, right, target)
                        if l == -1 and r == -1:
                            return -1
                        else:
                            return r if  r!= -1 else l
                    else:
                        return left
                else:
                    return right

        return bit_search(0, len(nums)-1, target)

'''
自己写的真是太复杂了，主要是我还是没考虑有序性的问题，如果差的话我自己写的是会退化成O(n)的
先看看 mid 左右两边排好没有， 判断排好的那一边，剩下的情况全是搜另一边的情况
最好的答案：
'''

class Solution(object):
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + ((high-low) >> 1)
            if target == nums[mid]: return mid
            if nums[low] <= nums[mid]:
                '''注意这个if 判断的等号要写，因为 low 和 mid可能下标相等'''
                #左边已排好
                if nums[low] <= target < nums[mid]:
                    high = mid -1
                else:
                    # target < nums[low] 或者 target > nums[mid] 要么被旋到右边要么 本身就在右边
                    low = mid + 1
            elif nums[low] >= nums[mid]:
                #左边没排好，但是右边排好了
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid -1
        return -1




'''
test case:
1. 
[3,1]
0
'''
a = Solution