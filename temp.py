class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end='->')
            temp = temp.next
        print()
 
 
# Tester class
llist = LinkedList()
llist.push(2)
llist.push(5)
llist.push(6)
llist.push(8)
 
print("Given Linked List:")
llist.printList()
llist.reverse()
print("Reversed Linked List:")
llist.printList()