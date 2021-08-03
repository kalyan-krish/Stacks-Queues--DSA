class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self,item):
        self.queue.append(item)
    
    def dequeue(self):
        if len(self.queue) == 0:
            return 'Queue is empty'
        
        self.queue.pop(0)
    
    def display(self):
        print(self.queue)
    
    def peek(self):
        size = len(self.queue)
        print(self.queue[size-1])
    
    
q =Queue()
q.enqueue(2)
q.enqueue(12)
q.enqueue(20)
q.display()
q.dequeue()
q.display()
q.peek()
