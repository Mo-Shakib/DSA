#-----------Binary Tree------------

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
btn1 = BinaryTreeNode(1)
btn2 = BinaryTreeNode(2)
btn3 = BinaryTreeNode(3)

btn1.left = btn2
btn1.right = btn3

