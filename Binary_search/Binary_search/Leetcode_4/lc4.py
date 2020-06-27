class Solution1(object):
    def findMedianSortedArrays(self, nums1, nums2):
        def find_kth(left1, right1,nums1, left2, right2,nums2, k):
            if right2 - left2 < right1 - left1:
                '''这个操作是保证 num1长度 <= num2 长度， 先用完的永远是num1 '''
                return find_kth(left2, right2, nums2, left1, right1, nums1,k)
            while left1 <= right1 and left2 <= right2:
                if k == 1:
                    return min(nums1[left1], nums2[left2])
                midK = k // 2
                mid1 = min(right1, left1 + midK-1)
                mid2 = min(right2, left2 + midK-1)
                '''这边的-1真的要注意一下，差点就错了'''
                if nums1[mid1] <= nums2[mid2]:
                    k -= mid1 - left1 + 1
                    left1 = mid1 + 1
                else:
                    k -= mid2 - left2 + 1
                    left2 = mid2 + 1
            #其中num1用完了才会跳出循环的, 否则会return
            return nums2[left2 + k - 1] if left2 <= right2 else nums1[left1 + k - 1]

        if len(nums1) == 0:
            return nums2[(len(nums2)-1)//2] if len(nums2) & 1 \
                else (nums2[(len(nums2)-1) // 2] + nums2[(len(nums2)-1)//2 + 1])*0.5
        if len(nums2) == 0:
            return self.findMedianSortedArrays(nums2, nums1)
        all_len = len(nums1) + len(nums2)
        '''
        如果中间值是 mid  = (all_len -1)//2 的话找的是左边下标（从0开始）
            比如[0,1,2] 找的是1 [0,1,2,3] 找的还是1
            算到0的时候找1个
            那么如何和个数进行转化呢？
        如果是 mid = (all_len + 1)// 2 找的就是第mid 个
            比如[0,1,2] 找的是第二个 [0,1,2,3] 找的就是 5/2 第二个
            算到 1 的时候找一个
        综上：做二分查找的时候要mid是要当下标还是要当排除的个数，这样才好算
            这道题这个方法是用个数来算的
        '''
        if all_len & 1 :
            return find_kth(0, len(nums1)-1, nums1, 0, len(nums2)-1, nums2, (all_len+1) // 2)
        else:
            left = all_len // 2
            right = all_len // 2 + 1
            return (find_kth(0, len(nums1)-1, nums1, 0, len(nums2)-1, nums2, left) + \
                    find_kth(0, len(nums1) - 1, nums1, 0, len(nums2) - 1, nums2, right)) * 0.5
'''
解法二
把 nums1 和 nums2 的数组合并起来，然后找一个划分 
使得 num1[i-1] < nums[j]
     num2[j-1]< nums[i]
     在 i-1 和 i , j-1 和 j 之间砍一刀分成左右数量相等的两块
注意这个划分可能找不到，比如 nums1 数量太少了而且太小/太大了直接用完了，这样就只能找nums2
那么如何找到这个划分？
用二分法在小的nums1里面找，找到之后就跳出循环，找不到就是特殊的状态啦
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) == 0:
            return nums2[(len(nums2)-1)//2] if len(nums2) & 1 \
                else (nums2[(len(nums2)-1) // 2] + nums2[(len(nums2)-1)//2 + 1])*0.5
        if len(nums1) > len(nums2):
            '''
            nums1 的长度一定要小于nums2 的长度
            因为 j-1 要大于0， 说明 nums1 比 nums2 快用完
            找分割的位置可以找小的长度，时间复杂度更低， 为 O(log(min(m,n)))
            '''
            return self.findMedianSortedArrays(nums2, nums1)

        left = 0
        right = len(nums1) - 1
        while left <= right:
            midi = left + (right - left + 1) // 2  # 偏大的那个下标, 表示它的左边还有多少个的意思
            midj = (len(nums1) + len(nums2) + 1) // 2 - midi
            ''' (i + j) + (i+j-1) = m + n  如果 m + n 是奇数的话
                如果是偶数的话 +1截断除也没有问题'''
            if nums1[midi] < nums2[midj - 1]:
                left = midi + 1
            elif midi >= 1  and nums1[midi-1] > nums2[midj]:
                right = midi - 1
            else:
                '''出循环的条件：
                1.找到了 midi 此时 left <= right != 0
                2.midi = right ==left== 0 切在左边界
                3.left = right + 1, right = len(nums1) 切在右边界
                （left 和 right 交错的时候一定是在右边界，否则就矛盾了）
                '''
                break
        nums1Index = midi if left <= right else left
        '''
        官方为了不写 nums1Index = midi or left 直接在循环的开始写了
        right = len(nums1)
        while (left <= right) 这样的话即使超过了右边界 left = right也会把所有的数组算上
        而一开始限制了边界 right = len(nums1) - 1的话就是left是左边数组的数的个数
        其实如果按划分nums1后左边个数来看的话边界问题没有那么复杂
        如果左边是n（left == n+1）个的话， 说明划分在 nums2 那里
        如果左边是0 个的话划分要么在nums1 这边要么在 nums2这边，看是否超过nums2的数量
        只用检测nums1就好啦，因为 nums2 永远比nums1 长
        
        '''
        nums2Index = (len(nums2) + len(nums1) + 1) // 2 - nums1Index
        if nums1Index == len(nums1) or nums1Index == 0:
            '''边界问题
             nums1Index == 0或者 == len的时候
             这两个要分开解决
            '''
            if nums1Index == 0:
                c1 = nums2[nums2Index - 1]
                c2 = min(nums1[nums1Index], nums2[nums2Index]) if nums2Index < len(nums2)else nums1[nums1Index]
            if nums1Index == len(nums1):
                c1 = max(nums1[nums1Index-1], nums2[nums2Index-1]) if nums2Index >= 1 else nums1[nums1Index-1]
                c2 = nums2[nums2Index]
            # c1 = max(nums1[nums1Index-1], nums2[nums2Index-1])if nums2Index != 0 and nums1Index == len(nums1) else nums1[nums1Index-1]
            # c2 = min(nums1[nums1Index], nums2[nums2Index]) if nums1Index == 0 and nums2Index!= len(nums2) else nums1[nums1Index]
        else:
            c1 = max(nums1[nums1Index-1], nums2[nums2Index-1])
            c2 = min(nums1[nums1Index], nums2[nums2Index])
        if (len(nums1)+len(nums2)) & 1:
            return c1
        return (c1 + c2) * 0.5



'''
test case:
1.
nums1 = [1]
nums2 = [3, 4]
这两个要一起看
nums1 = [2]
nums2 = [1,3]
2.
nums1 = [1000]
nums2 = [1001]
3.
nums1 = []
nums2 = [3, 4]
5.
nums1 = [5]
nums2 = [3, 4]
6.
nums1 = [2,3]
nums2 = [4,5]
and 
nums1 = [4,5]
nums2 = [2,3]
and
nums1 = [2,3]
nums2 = [  3,4,5]
'''
a = Solution()
nums2 = [5,6]
nums1 = [3, 4]
print(a.findMedianSortedArrays(nums1, nums2))
print("Done")




