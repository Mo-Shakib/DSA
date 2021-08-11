# Name: MD. SHAKIB MOLLA
# ID: 20301231
# Section: 05
# Lab assignment : 04
#-------------------------Task - 1--------------------------------
class ArrayStack:
    def __init__(self):
        self.data = []
    
    def is_empty(self):
        return len(self.data) == 0
    
    def push(self,val):
        self.data.append(val)
    
    def pop(self):
        if self.is_empty() == False:
        
            if len(self.data) == 1:
                temp = self.data[-1]
                self.data = self.data[:-1]
                return temp
            
            if len(self.data) > 1:
                temp = self.data[-1]
                self.data = self.data[:-1]
                return temp
    
    def clear(self):
        if self.data != []:
            self.data = []
    
    def checkBraket(self, a, b):
        if a == "(" and b == ")":
            return True
        if a == "{" and b == "}":
            return True
        if a == "[" and b == "]":
            return True
        return False
    
    def checkExpresion(self, expr):
        open = '([{'
        close = ')]}'
        i = 0
        for element in expr:
            if element in open:
                self.push((element, i))
            if element in close:
                if self.is_empty():
                    print('This expression is NOT correct')
                    print(f'Error at charactrt # {i+1}. "{element}" - not opened.')
                    return
                    
                temp = self.pop()
                
                if self.checkBraket(temp[0], element) == False:
                    print('This expression is NOT correct')
                    print(f'Error at charactrt # {temp[1]+1}. "{temp[0]}" -not closed.')
                    return
            i+= 1
                    
        if self.is_empty():
            print('This expression is correct')
            return
        
        if self.is_empty() == False:
            print('This expression is NOT correct')
            temp = self.pop()
            print(f'Error at charactrt # {temp[1]+1}. "{temp[0]}"-not closed.')

# a = ArrayStack()
# print('Input for task - 1: ')
# a.checkExpresion(input())

# -------------------------------Task - 2--------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:     
            node = Node(data)
            node.next = self.head
            self.head = node
        
    def pop(self):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            return temp
       
    def is_empty(self):
        return self.head is None
    
    def clearStack(self):
        x = self.head
        while x!= None:
            self.pop()
            x = x.next
    
    def checkBraket(self, a, b):
        if a == "(" and b == ")":
            return True
        if a == "{" and b == "}":
            return True
        if a == "[" and b == "]":
            return True
        return False


def checkExpresion(linkedListStack, expr):
    open = '([{'
    close = ')]}'
    
    i = 0
    for element in expr:
        if element in open:
            linkedListStack.push((element, i))
        if element in close:
            if linkedListStack.is_empty():
                print('This expression is NOT correct')
                print(f'Error at charactrt # {i+1}. "{element}" - not opened.')
                return
                
            temp = linkedListStack.pop()
            if linkedListStack.checkBraket(temp[0], element) == False:
                print('This expression is NOT correct')
                print(f'Error at charactrt # {temp[1]+1}. "{temp[0]}" -not closed.')
                return
        i+= 1
                
    if linkedListStack.is_empty():
        print('This expression is correct')
        return
    
    if linkedListStack.is_empty() == False:
        print('This expression is NOT correct')
        temp = linkedListStack.pop()
        print(f'Error at charactrt # {temp[1]+1}. "{temp[0]}"-not closed.')
        return
        
# linkedListStack = Stack()
# print("Input for task - 2:")
# checkExpresion(linkedListStack, input())

#------------------------- Taster ------------------------------------
test_cases = ['1+2*(3/4)', '1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14','1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14', '1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14']

# for task - 2
print('----------------- Task - 1 ---------------------')
a_stack = ArrayStack()
j = 1
for i in test_cases:
    print(f'Output {j}:')
    print(i)
    a_stack.checkExpresion(i)
    a_stack.clear()
    print()
    j += 1

# for task - 2
print('----------------- Task - 2 -------------------------')
linkedListStack = Stack()
a = 1
for i in test_cases:
    print(f'Output {a}:')
    print(i)
    checkExpresion(linkedListStack, i)
    linkedListStack.clearStack()
    print()
    a += 1