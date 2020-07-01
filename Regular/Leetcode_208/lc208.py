class Node:
    def __init__(self, val):
        self.val = val
        self.next = {}
        self.word_num = 0

class Trie(object):

    def __init__(self):
        self.root = Node('')

    def insert(self, word):
        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur.next:
                cur.next[word[i]] = Node(word[i])
            cur = cur.next[word[i]]
        cur.word_num += 1


    def search(self, word):
        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur.next: return False
            cur = cur.next[word[i]]
        return cur.word_num > 0


    def startsWith(self, prefix):
        cur = self.root
        for i in range(len(prefix)):
            if prefix[i] not in cur.next: return False
            cur = cur.next[prefix[i]]
        return True


'''
我写的还是太冗余了， 去others 里面是前缀树的标准写法
'''