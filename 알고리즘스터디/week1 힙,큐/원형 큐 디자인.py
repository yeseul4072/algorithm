class MyCircularQueue:

    def __init__(self, k: int):
        self.maxlen = k
        self.q = [None] * k
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True
        return False

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.p1]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        if self.p2 == 0:
            return self.q[self.maxlen - 1]
        return self.q[self.p2 - 1]

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()