from enum import Enum
from chapter1.MyStack import Stack


def hanoiProblem1(num, left, mid, right):
    if num < 1:
        return 0
    return process(num, left, mid, right, left, right)


def process(num, left, mid, right, from_, to_):
    if num == 1:
        print('Move 1 from %s to %s' % (from_, mid))
        print('Move 1 from %s to %s' % (mid, to_))
        return 2
    part1 = process(num - 1, left, mid, right, from_, to_)
    part2 = 1
    print('Move %d from %s to %s ' % (num, from_, mid))
    part3 = process(num - 1, left, mid, right, to_, from_)
    part4 = 1
    print('Move %d from %s to %s ' % (num, mid, to_))
    part5 = process(num - 1, left, mid, right, from_, to_)
    return part1 + part2 + part3 + part4 + part5


class Action(Enum):
    no = 1
    ltoM = 2
    mtoL = 3
    rtoM = 4
    mtoR = 5


def hanoiProblem2(num, left, mid, right):
    ls = Stack()
    ms = Stack()
    rs = Stack()
    ls.push(2147483647)
    ms.push(2147483647)
    rs.push(2147483647)
    for i in range(num, 0, -1):
        ls.push(i)
    record = [Action.no]
    steps = 0
    while rs.size() != num + 1:
        steps += fStackToStack(record, Action.mtoL, Action.ltoM, ls, ms, left, mid)
        steps += fStackToStack(record, Action.ltoM, Action.mtoL, ms, ls, mid, left)
        steps += fStackToStack(record, Action.rtoM, Action.mtoR, ms, rs, mid, right)
        steps += fStackToStack(record, Action.mtoR, Action.rtoM, rs, ms, right, mid)
    return steps


def fStackToStack(record, preNoAct, nowAct, fStack, tStack, from_, to_):
    if record[0] != preNoAct and fStack.peek() < tStack.peek():
        tStack.push(fStack.pop())
        print("Move %d from %s to %s" % (tStack.peek(), from_, to_))
        record[0] = nowAct
        return 1
    return 0


if __name__ == '__main__':
    num = 3
    steps = hanoiProblem1(num, 'left', 'mid', 'right')
    print('It will take %d steps' % (steps))
    print("=====================")
    steps2 = hanoiProblem2(3, 'left', 'mid', 'right')
    print('It will take %d steps' % (steps2))
