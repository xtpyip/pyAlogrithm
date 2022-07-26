class LinkedList(object):
    def __init__(self):
        self.data = []

    def pollFirst(self):
        if self.isEmpty():
            raise RuntimeError("Your linkedList is empty")
        return self.data.pop(0)

    def pollLast(self):
        if self.isEmpty():
            raise RuntimeError("Your linkedList is empty")
        return self.data.pop()

    def addFirst(self, value):
        self.data.insert(0, value)

    def addLast(self, value):
        self.data.append(value)

    def isEmpty(self):
        return len(self.data) == 0

    def peekFirst(self):
        return self.data[0]

    def peekLast(self):
        return self.data[-1]
