class Queue(object):
    def __init__(self):
        self.queue = []

    def add(self, value):
        self.queue.append(value)

    def poll(self):
        if self.is_empty():
            raise RuntimeError("your queue is empty")
        else:
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0
