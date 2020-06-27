
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def getList(l):
    if len(l) == 0:
        return None
    head = ListNode(0)
    cur = head
    for val in l:
        cur.next = ListNode(val)
        cur = cur.next
    return head.next
def printList(l):
    if l == None:
        return []
    else:
        res = []
        cur = l
        while cur:
            res.append(cur.val)
            cur = cur.next
        print(res)

if __name__ == "__main__":
    l = [1,2,3,4,5]
    myList = getList(l)
    print(printList(myList))
    print("Done!")
