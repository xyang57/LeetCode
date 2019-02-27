"""
Queue implementation using two stacks
"""
class QueuefromStacks():
    def __init__(self):
        self.instack = []
        self.outstack = []
    
    def enqueue(self,x):
        self.instack.append(x)
        
    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()
        
                