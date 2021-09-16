# Queue implementation using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class Queue:
    def __init__(self):
        self.head = None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    def dequeue(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            return temp.data
    
    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end = ' ')
            temp = temp.next
        print()
        
    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data
        

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.print()
queue.enqueue(3)
queue.print()
print(queue.dequeue())
queue.print()
print(queue.peek())