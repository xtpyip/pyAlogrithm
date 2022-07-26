from chapter1.MyStack import Stack


def sort_stack_by_stack(stack):
    helper = Stack()
    while not stack.is_empty():
        cur = stack.pop()
        while (not helper.is_empty()) and helper.peek() > cur:
            stack.push(helper.pop())
        helper.push(cur)
    while not helper.is_empty():
        stack.push(helper.pop())


if __name__ == '__main__':
    test = Stack()
    test.push(7)
    test.push(5)
    test.push(8)
    test.push(3)
    test.push(9)
    test.push(2)
    test.push(6)
    sort_stack_by_stack(test)
    print(test.pop())
    print(test.pop())
    print(test.pop())
    print(test.pop())
    print(test.pop())
    print(test.pop())
    print(test.pop())