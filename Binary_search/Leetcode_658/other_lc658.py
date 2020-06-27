class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        low = 0
        high = len(arr) - k
        while low <high:
            mid = low + (high-low)//2
            if x - arr[mid]  > arr[mid+k] - x:
                low = mid+1 # 不包含mid的滑动窗口
            elif x - arr[mid] == arr[mid + k] - x:
                high = mid #包含mid的滑动窗口
            elif x - arr[mid] < arr[mid+k] - x:
                high = mid
        return arr[low:low+k]
    '''
    这个用二分代替指针对撞滑动窗口真的好骚啊，直接去掉了一半的数
    '''