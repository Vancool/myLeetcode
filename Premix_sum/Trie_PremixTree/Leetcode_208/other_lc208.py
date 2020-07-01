class Node:
    def __init__(self):
        self.next = {}
        # 这边可以用26大小的数组代替哈希表， 只是要用ord 做映射
        self.word_num = 0

class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root
        for w in word:
            if w not in cur.next:
                cur.next[w] = Node()
            cur = cur.next[w]
        cur.word_num += 1


    def search(self, word):
        cur = self.root
        for w in word:
            if w not in cur.next: return False
            cur = cur.next[w]
        return cur.word_num > 0


    def startsWith(self, prefix):
        cur = self.root
        for p in prefix:
            if p not in cur.next: return False
            cur = cur.next[p]
        return True