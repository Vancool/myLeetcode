class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        '''
        二分法解题，这一题非常好
        二分法不需要递归，直接一个循环就好
        两次二分查找寻找左右边界下标
        这两次二分法不能合起来
        注意这两次循环中左右下标对arr[mid] == target时候的处理
        '''
        #找l_bound
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = left + (right-left)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                #== target
                '''
                left 下标不动，right往左走
                如果左边数组全部都很大的话最终right会一直不动left往右走直至与right重合
                因此最终left的下标会在左边界停下
            '''
                right = mid - 1
        l_bound = left

        #找h_bound
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                left = mid + 1
                '''
                right 最终会走到下标位置，而left会在下标+1的位置
                '''
        h_bound = right
        return  h_bound - l_bound + 1










