# Example of a LinkedList

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def printNode(self):
        print(self.value, '-', self.next)

class LinkedList:
    def __init__(self, a):
        self.head = None
        tail = None

        for i in a:
            n = Node(i, None)
            if (self.head is None):
                self.head = n
                tail = n
            else:
                tail.next = n
                tail = n

    def printList(self):
        n = self.head
        while (n is not None):
            n.printNode()
            n = n.next

# ------Taster class --------------------------------

list1 = [1, 2, 3, 4, 5]
list2 = LinkedList(list1)

list2.printList()
