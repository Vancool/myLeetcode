class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    count = 0
    def Serialize(self, root):
        # write code here
        if root == None:
            return '#'
        s1 = self.Serialize(root.left)
        s2 = self.Serialize(root.right)
        return str(root.val) + ','+ s1 +',' + s2
    def Deserialize(self, str1):
        # write code here
        s = str1.split(',')
        if self.count >= len(s) or s[self.count] == '#':
            self.count += 1
            return None
        root = TreeNode(int(s[self.count]))
        self.count += 1
        root.left = self.Deserialize(str1)
        root.right = self.Deserialize(str1)
        return root


a = Solution()

