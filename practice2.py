class Node:
    def __init__(self, value, next, previous):
        self.value = value
        self.nextAddress = next
        self.prevAddress = previous


class DoublyList:
    def __init__(self, a):
        if len(a) == 0:
            print("Array cannot be empty")
        else:
            self.head = None
            dummyHead = Node(None, None, None)
            self.head = dummyHead
            object = None
            next = dummyHead
            prev = dummyHead
            for i in a:
                object = Node(i, None, None)
                object.prevAddress = prev
                prev = object
                next.nextAddress = object
                next = object
            object.nextAddress = dummyHead
            dummyHead.prevAddress = object

    def showList(self):
        object = self.head.nextAddress
        if object.value == None:
            print("Empty List")
        else:
            while object != self.head:
                print(object.value, end="->")
                object = object.nextAddress
            print()


list1 = DoublyList([4, 5, 3])
list2 = DoublyList([9, 5, 2])


def sum(*list):
    sum = 0
    for i in (list):
        x = ""
        obj = i.head.nextAddress
        while obj.value != None:
            x += str(obj.value)
            obj = obj.nextAddress
        x = int(x)
        sum += x

    list = []
    for k in str(sum):
        list += [k]
    newNode = DoublyList(list)
    return newNode


list3 = sum(list1, list2)
list3.showList()
