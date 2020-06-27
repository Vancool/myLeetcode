def findKthLargest(self, nums, k):
    return self.quickSelect(nums, 0, len(nums) - 1, k)


def quickSelect(self, nums, start, n, k):  # quick select
    pos = self.partition(nums, start, n)
    if pos == k - 1:
        return nums[pos]
    elif pos >= k:
        return self.quickSelect(nums, start, pos - 1, k)
    return self.quickSelect(nums, pos + 1, n, k)


def partition(self, nums, left, right):
    pivot = nums[right]  # pick the last one as pivot
    print(pivot)
    i = left
    print(i)
    for j in range(left, right):  # left to right -1
        if nums[j] > pivot:  # the larger elements are in left side
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
            print(nums)
    nums[right], nums[i] = nums[i], nums[right]  # swap the i and the last element
    print(nums)
    return i

def singleNumber(self, nums):

    if (len(nums) == 1):
        return nums[0]
    for i in nums:
        nums.remove(i)
        nums = nums - i
        if 0 in nums:
            nums.remove(0)
        else:
            return i

    return 0  # find False

if __name__ == "__main__":
    for i in range(10):
        print(i)
        if i ==2:
            i = i + 1
            print("count")
            print(i)

