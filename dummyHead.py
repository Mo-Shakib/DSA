class Node:
    def __init__(self, e, n, p):
        self.element = e
        self.next = n
        self.prev = p


class DoublyList():
    def __init__(self,a):
        self.head = Node(None, None, None)
        self.head.next = self.head.prev = self.head
        start = self.head
        for x in a:
            n = Node(x, None, None)
            n.next = start.next
            n.prev = start
            start.next = n
            n.next.prev = n
            start = n