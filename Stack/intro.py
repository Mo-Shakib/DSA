# Introduction to Stack

class Stack:
    def __init__(self):
        self.items = [0] * 5
        self.size = 0
        self.lenth  = len(self.items)

    # a method to print the stack
    def display(self):
        print(self.items)

    # pushing an element to the array
    def push(self, item): 
        n = len(self.items)
        for i in self.items:
            if i != 0:
                n -= 1
        if n <= 0:
            print('No more space in this Stack!')
        else:
            for i in range(len(self.items)):
                if self.items[i] == 0:
                    self.items[i] = item
                    return

    # a method to remove the last item from the stack and make the value 0
    def pop(self):
        x = 0
        if self.items[0] == 0:
            print('The Stuck is already empty!')
            return

        for i in range(len(self.items)):
            if self.items[i] == 0:
                self.items[i-1] = 0
                print('Removed an item')
                x = 1
                break
        if x == 0:
            self.items[-1] = 0
            print('Removed an item')            

    # create an method to return the last item from the stack
    def peek(self):
        return self.items[-1]


s = Stack()
s.push(1)
s.display()
s.pop() #1
s.display()
s.pop() #1
s.display()
s.push(1)
s.push(2)
s.push(3)
s.display()