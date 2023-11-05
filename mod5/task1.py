class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def pop(self):
        if self.is_empty():
            return None
        value = self.top.data
        self.top = self.top.next
        return value

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node

    def print(self):
        current = self.top
        while current:
            print(current.data, end=" ")
            current = current.next
        print("None")


stack = Stack()
stack.push(4)
stack.push(5)
stack.push(6)

stack.print()

popped = stack.pop()
print("Popped element:", popped)

stack.print()
