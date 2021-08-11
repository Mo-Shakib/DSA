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

    def checkBraket(self, a, b):
        if a == "(" and b == ")":
            return True
        if a == "{" and b == "}":
            return True
        if a == "[" and b == "]":
            return True
        return False

    def clearStack(self):
        x = self.head
        while x!= None:
            self.pop()
            x = x.next


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
                print(f'Error at charactrt # {i + 1}. "{element}" - not opened.')
                return

            temp = linkedListStack.pop()

            if linkedListStack.checkBraket(temp[0], element) == False:
                print('This expression is NOT correct')
                print(f'Error at charactrt # {temp[1] + 1}. "{temp[0]}" -not closed.')
                return
        i += 1

    if linkedListStack.is_empty():
        print('This expression is correct')
        return

    if linkedListStack.is_empty() == False:
        print('This expression is NOT correct')
        temp = linkedListStack.pop()
        print(f'Error at charactrt # {temp[1] + 1}. "{temp[0]}"-not closed.')


"""
checkExpresion(linkedListStack,'1+2*(3/4)' )
linkedListStack.clearStack()
checkExpresion(linkedListStack, '1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14')
linkedListStack.clearStack()
checkExpresion(linkedListStack, '1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14')
linkedListStack.clearStack()
checkExpresion(linkedListStack, '1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14')"""

linkedListStack = Stack()
test_cases = ['1+2*(3/4)', '1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14','1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14', '1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14']

a = 1
for i in test_cases:
    print(f'Output {a}:')
    print(i)
    checkExpresion(linkedListStack, i)
    linkedListStack.clearStack()
    print()
    a += 1