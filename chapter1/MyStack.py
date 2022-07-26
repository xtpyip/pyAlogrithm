class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, new_value):
        self.stack.append(new_value)

    def pop(self):
        if len(self.stack) == 0:
            raise Exception("your stack is empty")
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            raise Exception("your stack is empty")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)