class MyStack(object):
    def __init__(self):
        self.lst = list()

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)


class MyQueue(object):
    def __init__(self, max_size):
        self.stack1 = MyStack()
        self.stack2 = MyStack()
        self.max_size = max_size

    def qsize(self):
        # 구현하세요
        return max(self.stack1.size(), self.stack2.size())

    def push(self, item):
        # 구현하세요
        while self.stack2.size():
            self.stack1.push(self.stack2.pop())
        if self.stack1.size() >= max_size:
            return False
        self.stack1.push(item)
        return True

    def pop(self):
        # 구현하세요
        while self.stack1.size():
            self.stack2.push(self.stack1.pop())
        if self.stack2.size():
            return self.stack2.pop()
        return False


n, max_size = map(int, input().strip().split(' '))
my_queue = MyQueue(max_size)
for _ in range(n):
    arr = input().split()
    if arr[0] == 'SIZE':
        print(my_queue.qsize())
    elif arr[0] == 'POP':
        print(my_queue.pop())
    else:
        print(my_queue.push(arr[1]))
