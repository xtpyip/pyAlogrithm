from chapter1.MyStack import Stack


class TwoStacksQueue(object):
    def __init__(self):
        self.stackPush = Stack()
        self.stackPop = Stack()

    def add(self, value):
        self.stackPush.push(value)

    def poll(self):
        if self.stackPush.is_empty() and self.stackPop.is_empty():
            raise RuntimeError("Your stack is empty")
        elif self.stackPop.is_empty():
            while not self.stackPush.is_empty():
                self.stackPop.push(self.stackPush.pop())
        return self.stackPop.pop()

    def peek(self):
        if self.stackPush.is_empty() and self.stackPop.is_empty():
            raise RuntimeError("Your stack is empty")
        elif self.stackPop.is_empty():
            while not self.stackPush.is_empty():
                self.stackPop.push(self.stackPush.pop())
        return self.stackPop.peek()


if __name__ == '__main__':
    test = TwoStacksQueue()
    test.add(1)
    test.add(2)
    test.add(3)
    print(test.peek())
    print(test.poll())
    print(test.peek())
    print(test.poll())
    print(test.peek())
    print(test.poll())
