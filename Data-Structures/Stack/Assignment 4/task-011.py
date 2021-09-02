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
                # if close.index(element) != open.index(self.pop()):
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

a = ArrayStack()
a.checkExpresion(input())