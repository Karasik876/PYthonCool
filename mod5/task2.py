class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        new_node.next = self.rear
        self.rear.prev = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.front.value
        self.front = self.front.prev
        if self.front is None:
            self.rear = None
        else:
            self.front.next = None
        return value

    def display(self):
        current = self.rear
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


queue = Queue()
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(7)
queue.enqueue(8)

queue.display()

dequeued = queue.dequeue()
print("Dequeued element:", dequeued)

queue.display()