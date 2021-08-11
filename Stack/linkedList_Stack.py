
# Stack implementation using Linkedlist

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        

    def pop(self):
        if self.head is None:
            return
        else:
            popped = self.head
            self.head = self.head.next
            popped.next = None
            popped.data = None
            

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def showStack(self):
        if self.head is None:
            print("Empty Stack")
        else:
            temp = self.head
            while temp:
                print(temp.data, end='->')
                temp = temp.next
            print()
    
stack = Stack()
stack.push(10)
stack.push(20)
stack.showStack()
stack.push(30)
stack.showStack()
stack.pop()
stack.pop()
stack.pop()
stack.showStack()
stack.push(100)
stack.showStack()