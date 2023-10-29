class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.top.value

    def display(self):
        current = self.top
        while current:
            print(current.value, end=" ")
            current = current.next
        print("None")


stack = Stack()
stack.push(4)
stack.push(5)
stack.push(6)

stack.display()

print("Top element:", stack.peek())

popped = stack.pop()
print("Popped element:", popped)

stack.display()