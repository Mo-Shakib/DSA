# A Linked List Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 

# Function to print a given linked list
def printList(head):
 
    ptr = head
    while ptr:
        print(ptr.data, end=" —> ")
        ptr = ptr.next
    print("None")

# Iterate through the list and move/insert each node
# in front of the out list like `push()` of the node
def reverse(head):
    out = None
    current = head
    # traverse the list
    while current:
        # tricky: note the next node
        next = current.next
        # move the current node onto the out
        current.next = out
        out = current
        # process next node
        current = next
    # fix head
    return out

 
# Function to add two lists, `A` and `B`
def append(A, B):
 
    head = None
 
    # stores the last seen node
    prev = None
 
    # initialize carry with 0
    carry = 0
 
    # run till both lists are empty
    while A or B:
 
        # sum is A's data + B's data + carry (if any)
        sum = 0
        if A:
            sum += A.data
        if B:
            sum += B.data
 
        sum += carry
 
        # if the sum of a 2-digit number, reduce it and update carry
        carry = sum // 10
        sum = sum % 10
 
        # create a new node with the calculated sum
        node = Node(sum, None)
 
        # if the output list is empty
        if head is None:
            # update `prev` and `head` to point to the new node
            prev = node
            head = node
        else:
            # add the new node to the output list
            prev.next = node
 
            # update the previous node to point to the new node
            prev = node
 
        # advance `A` and `B` for the next iteration of the loop
        A = A.next if A else A
        B = B.next if B else B
 
    if carry:
        prev.next = Node(carry, prev.next)
 
    return head
 
 
# Function to add two lists, `A` and `B`
def addLists(A, B):
 
    # reverse `A` and `B` to access elements from the end
    A = reverse(A)
    B = reverse(B)
 
    return reverse(append(A, B))

if __name__ == '__main__':
 	# Input numbers given here.
    x = 453
    y = 952
 
    # construct list `A` (4 —> 5 —> 3) from number `x`
    A = None
    while x:
        A = Node(x % 10, A)
        x = x // 10
 
    # construct list `B` (9 —> 5 —> 2) from number `y`
    B = None
    while y:
        B = Node(y % 10, B)
        y = y // 10
 
    printList(addLists(A, B))