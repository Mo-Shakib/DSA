# create a stuck class and its methords
class Stack:
    def __init__(self):
        self.stack = []
        self.pointer = -1

    def push(self, data):
        self.stack.append(data)
        self.pointer += 1

    def pop(self):
        if self.pointer == -1:
            return
        else:
            temp = self.stack[self.pointer]
            self.stack = self.stack[:-1]
            self.pointer -= 1
            return temp

    def peek(self):
        return self.stack[self.pointer]

    def isEmpty(self):
        if self.pointer == -1:
            return True
        else:
            return False

    def showStack(self):
        print(self.stack)

a = Stack()
a.showStack()
a.push(1)
a.push(2)
a.showStack()
a.pop()
a.showStack()
a.pop()
a.showStack()
a.pop()