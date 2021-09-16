# Queue implemenation using array

class Queue:
    def __init__(self):
        self.data = []
    
    def enqueue(self, item):
        self.data.append(item)
    
    def dequeue(self):
        if self.data == []:
            return None
        else:
            x = self.data[0]
            self.data = self.data[1:]
            return x
    
    def peek(self):
        if self.data == []:
            return None
        return self.data[0]
    

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.data)