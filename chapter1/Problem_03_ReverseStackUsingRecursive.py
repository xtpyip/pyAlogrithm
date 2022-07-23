from chapter1.MyStack import Stack


class ReverseStack(object):
    def __init__(self):
        self.stack = Stack()
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)

    def getAndRemoveElement(self):
        result = self.stack.pop()
        if self.stack.is_empty():
            return result
        else:
            last = self.getAndRemoveElement(self.stack)
            self.stack.push(result)
            return last

    def recursive(self):
        if self.stack.is_empty:
            return
        value = self.getAndRemoveElement(self.stack)
        self.recursive(self.stack)
        self.stack.push(value)

    def print(self):
        while not self.stack.is_empty():
            print(self.stack.pop(), end="\t")


if __name__ == '__main__':
    test = ReverseStack()
    test.recursive()
    test.print()
