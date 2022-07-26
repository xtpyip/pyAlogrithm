from chapter1.MyLinkedList import LinkedList


def getMaxValueOfSlidingWindow(arr, w):
    if arr == None or w <= 0 or len(arr) < w:
        return None
    linkedList = LinkedList()
    res = []
    for i in range(0,len(arr)):
        while (not linkedList.isEmpty()) and (arr[linkedList.peekLast()] < arr[i]):
            linkedList.pollLast()
        linkedList.addLast(i)
        if linkedList.peekFirst() == i - w:
            linkedList.pollFirst()
        if i >= w - 1:
            res.append(arr[linkedList.peekFirst()])
    return res


# for test
def printArray(arr):
    for i in range(0, len(arr)):
        print(arr[i], end='\t')
    print()


if __name__ == '__main__':
    arr = [4, 3, 5, 4, 3, 3, 6, 7]
    w = 3
    printArray(arr)
    result = getMaxValueOfSlidingWindow(arr, w)
    printArray(result)
