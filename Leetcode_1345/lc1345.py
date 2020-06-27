class Solution(object):
    def minJumps(self, arr):
        if len(arr) < 2: return 0
        if arr[0] == arr[-1] or len(arr) == 2: return 1


'''
这题有思路，但是不太会做
'''