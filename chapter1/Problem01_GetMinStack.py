
from chapter1.MyStack import Stack

class MyStack1(object):
    def __init__(self):
        self.stackMin = Stack()
        self.stackData = Stack()

    def push(self, new_value):
        if self.stackMin.is_empty():
            self.stackMin.push(new_value)
        elif new_value <= self.stackMin.peek():
            self.stackMin.push(new_value)
        self.stackData.push(new_value)

    def pop(self):
        if self.stackData.is_empty():
            raise Exception("Your stack is empty")
        value = self.stackData.pop()
        if value == self.stackMin.peek():
            self.stackMin.pop()
        return value

    def peek(self):
        if self.stackMin.is_empty():
            raise Exception("Your stack is empty")
        return self.stackMin.peek()

    def get_min(self):
        if self.stackMin.is_empty():
            raise Exception("Your stack is empty")
        return self.stackMin.peek()

    def print(self):
        while not self.stackMin.is_empty():
            print(self.stackMin.pop(), end="\t")


class MyStack2(object):
    def __init__(self):
        self.stackMin = Stack()
        self.stackData = Stack()

    def push(self, new_value):
        if self.stackMin.is_empty():
            self.stackMin.push(new_value)
        elif new_value <= self.stackMin.peek():
            self.stackMin.push(new_value)
        else:
            self.stackMin.push(self.stackMin.peek())
        self.stackData.push(new_value)

    def pop(self):
        if self.stackData.is_empty():
            raise Exception("Your stack is empty")
        self.stackMin.pop()
        return self.stackData.pop()

    def peek(self):
        if self.stackMin.is_empty():
            raise Exception("Your stack is empty")
        return self.stackMin.peek()

    def get_min(self):
        if self.stackMin.is_empty():
            raise Exception("Your stack is empty")
        return self.stackMin.peek()

    def print(self):
        while not self.stackMin.is_empty():
            print(self.stackMin.pop(), end="\t")


if __name__ == '__main__':
    mystack1 = MyStack1()
    mystack1.push(3)
    print(mystack1.peek())
    print(mystack1.get_min())
    mystack1.push(4)
    print(mystack1.peek())
    print(mystack1.get_min())
    mystack1.push(1)
    print(mystack1.peek())
    print(mystack1.get_min())
    mystack1.push(3)
    print(mystack1.peek())
    print(mystack1.get_min())
    print(mystack1.pop())
    print(mystack1.peek())
    print(mystack1.get_min())
    print(mystack1.pop())
    print(mystack1.peek())
    print(mystack1.get_min())
    mystack1.print()
    print("================================")
    mystack1 = MyStack2()
    mystack1.push(3)
    print(mystack1.peek())
    print(mystack1.get_min())
    mystack1.push(4)
    print(mystack1.peek())
    print(mystack1.get_min())
    mystack1.push(1)
    print(mystack1.peek())
    print(mystack1.get_min())
    mystack1.push(3)
    print(mystack1.peek())
    print(mystack1.get_min())
    print(mystack1.pop())
    print(mystack1.peek())
    print(mystack1.get_min())
    mystack1.print()
