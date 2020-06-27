class MyQueue:
    length = 0
    queue = None
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length =0
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)
        self.length += 1


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.length == 0:
            return 0
        res = self.queue[0]
        for i in range(1,self.length):
            self.queue[i-1] = self.queue[i]
        self.length -= 1
        return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        if(self.length == 0):
            return 0
        else:
            return self.queue[0]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.length == 0