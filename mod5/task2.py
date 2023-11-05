class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def is_empty(self):
        return self.start is None

    def push(self, value):
        new_node = Node(value)
        if self.end is None:
            self.start = self.end = new_node
            return
        new_node.next = self.end
        self.end.prev = new_node
        self.end = new_node

    def pop(self):
        if self.is_empty():
            return None
        value = self.start.data
        self.start = self.start.prev
        if self.start is None:
            self.end = None
        else:
            self.start.next = None
        return value

    def print(self):
        current = self.end
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


queue = Queue()
queue.push(4)
queue.push(5)
queue.push(7)
queue.push(8)

queue.print()

dequeued = queue.pop()
print("Dequeued element:", dequeued)

queue.print()
