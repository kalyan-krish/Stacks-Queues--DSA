def create_stack():
    stack=[]
    return stack

def push(stack,item):
    stack.append(item)
    print('The appended item is: '+ str(item))

def pop(stack):
    if (len(stack)==0): #checking the stack is empty 
        return 'Stack is empty'
    
    else:
        return stack.pop()

stack = create_stack()
print(pop(stack))
push(stack,2)
push(stack,12)
print(pop(stack))









Stack with classes:
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

s= Stack()
s.push(2)
s.push(12)
s.push(20)
print(s.peek())
print(s.size())
print(s.pop())
        

from pythonds.basic import Stack

s=Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
