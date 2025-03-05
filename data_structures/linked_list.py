class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        newNode = Node(data)
        
        if not self.head:
            self.head = newNode
            return
        last = self.head
        
        while last.next:
            last = last.next
        last.next = newNode
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.display()