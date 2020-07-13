class Solution(object):
    def kthSmallest(self, matrix, k):
        def binary_search(k, n):
            left_right = [matrix[n][i] for i in range(n)]
            top_bottom = [matrix[i][n] for i in range(n)]
            left, top = 0, 0
            right, bottom = n-1, n-1
            while k > 0:
                mid_left_right = -1
                mid_top_bottom = -1
                tmp = 0
                if left <= right:
                    mid_left_right = left + (right-left) // 2
                    tmp += (right-left+2)//2
                if top <= bottom:
                    tmp += (bottom-top+2)//2
                    mid_top_bottom = top + (bottom-top) // 2
                if mid_left_right >= 0 and mid_top_bottom >= 0:
                    if tmp > k+1:
                        if left_right[mid_left_right] > top_bottom[mid_top_bottom]:
                            k -= (right-left+1)//2
                            right = mid_left_right
                        else:
                            k -= (bottom-top+1)//2
                            bottom = mid_top_bottom
                    elif tmp < k+1:
                        if left_right[mid_left_right] < top_bottom[mid_top_bottom]:
                            k -= (right-left+2)//2
                            left = mid_left_right+1
                        else:
                            k -= (bottom-top+2)//2
                            top = mid_top_bottom+1
                    else:
                        return max(left_right[mid_left_right], top_bottom[mid_top_bottom])
                elif mid_left_right > 0:
                    return left_right[k]
                else:
                    return top_bottom[k]
            return min(left_right[left], top_bottom[top])
        sq_k = int(k ** 0.5)
        if sq_k ** 2 == k:
            return matrix[sq_k-1][sq_k-1]
        k -= sq_k**2
        return binary_search(k-1, sq_k)

'''
啊， 这个二分法， 我想错了。
我以为只要找到两个分割值，就可以转化为中间夹层数组的二分
原来不是的，比如：
[[1,3,5],
[6,7,12],
[11,14,14]]
k = 3
就要看 6 11 3 5 也就是7的左下角和右上角
'''
a = Solution()
matrix = [[1,3,5],[6,7,12],[11,14,14]]
k = 3
print(a.kthSmallest(matrix,k))





