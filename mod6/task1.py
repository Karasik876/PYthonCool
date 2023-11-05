class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, index):
        if index < 0:
            return None
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current.data if current else None

    def remove(self, index):
        if index < 0 or not self.head:
            return

        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index - 1):
                if current is None or current.next is None:
                    return
                current = current.next
            if current.next:
                current.next = current.next.next

    def insert(self, n, data):
        if n < 0:
            return

        new_node = Node(data)

        if n == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for i in range(n - 1):
                if current is None:
                    return
                current = current.next
            if current:
                new_node.next = current.next
                current.next = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

my_list = LinkedList()

my_list.push(4)
my_list.push(5)
my_list.push(6)

print("Список:")
for item in my_list:
    print(item)

print("Get(1):", my_list.get(1))
my_list.remove(0)
print("Список после удаления элемента с индексом 0:")
for item in my_list:
    print(item)

my_list.insert(1, 7)
print("Список после вставки в индекс 1:")
for item in my_list:
    print(item)