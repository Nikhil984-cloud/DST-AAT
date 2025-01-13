class Queue_Using_two_Stacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        
        self.stack1.append(value)

    def dequeue(self):
        if not self.stack2
      
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        if not self.stack2:
            return "Queue is empty"
        
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return "Queue is empty"
        return self.stack2[-1]

    def is_empty(self):
        return not self.stack1 and not self.stack2

queue = Queue_Using_two_Stacks()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())
print(queue.dequeue())

print(queue.peek())   

print(queue.is_empty()) 


print(queue.dequeue())


print(queue.is_empty()) 
