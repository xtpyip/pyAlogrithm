from chapter1.MyNode import Node
from chapter1.MyStack import Stack


def getMaxTree(arr):
    nArr = []
    for i in range(len(arr)):
        nArr.append(Node(arr[i]))
    stack = Stack()
    lBigMap = dict()
    rBigMap = dict()
    for i in range(len(arr)):
        curNode = nArr[i]
        while (not stack.is_empty()) and (stack.peek().value < curNode.value):
            popStackSetMap(stack, lBigMap)
        stack.push(curNode)
    while not stack.is_empty():
        popStackSetMap(stack, lBigMap)

    for i in range(len(arr) - 1, -1, -1):
        curNode = nArr[i]
        while (not stack.is_empty()) and (stack.peek().value < curNode.value):
            popStackSetMap(stack, rBigMap)
        stack.push(curNode)
    while not stack.is_empty():
        popStackSetMap(stack, rBigMap)

    head = None
    for i in range(len(arr)):
        curNode = nArr[i]
        left = lBigMap.__getitem__(curNode)
        right = rBigMap.__getitem__(curNode)
        if left == None and right == None:
            head = curNode
        elif left == None:
            if right.left == None:
                right.left = curNode
            else:
                right.right = curNode
        elif right == None:
            if left.left == None:
                left.left = curNode
            else:
                left.right = curNode
        else:
            if left.value < right.value:
                parent = left
            else:
                parent = right
            if parent.left == None:
                parent.left = curNode
            else:
                parent.right = curNode
    return head


def popStackSetMap(stack, map):
    curNode = stack.pop()
    if stack.is_empty():
        map.__setitem__(curNode, None)
    else:
        map.__setitem__(curNode, stack.peek())


# 前序遍历
def preOrder(head):
    if head == None:
        return
    print(head.value, end=" ")
    preOrder(head.left)
    preOrder(head.right)

    pass


# 中序遍历
def inOrder(head):
    if head == None:
        return
    inOrder(head.left)
    print(head.value, end=" ")
    inOrder(head.right)


if __name__ == '__main__':
    arr = [3, 4, 5, 1, 2]
    head = getMaxTree(arr)
    preOrder(head)
    print()
    inOrder(head)
