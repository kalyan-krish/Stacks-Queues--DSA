
class Circularqueue():
    def __init__(self,k):
        self.k=k
        self.queue = [None]*k
        self.head = self.tail = -1
    
    def enqueue(self,item):
        if ((self.tail+1) % self.k == self.head):
            print('Circular queue is full')
            
        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = item
        
        else:
            self.tail = (self.tail+1) % self.k 
            self.queue[self.tail] = item
    
    def dequeue(self):
        if self.head == -1:
            print('Queue is empty')
        elif self.head == self.tail:
            temp = self.queue[self.head]
            self.head = -1
            self.head = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head+1) % self.k
            return temp
    
    def printqueue(self):
        if self.head == -1:
            print('Queue is empty')
        
        elif (self.tail >= self.head):
            for i in range(self.head,self.tail+1):
                print(self.queue[i],end =' ')
            print()
        
        else:
            for i in range(self.head,self.k):
                print(self.queue[i],end = ' ')
            for i in range(0,self.tail+1):
                print(self.queue[i],end = ' ')
            print()
        
            
q = Circularqueue(5)   
q.enqueue(20)
q.enqueue(12)
q.enqueue(2) 
q.enqueue(11)
q.enqueue(21)
#print(q.dequeue())
#print(q.dequeue())
q.printqueue()
        
