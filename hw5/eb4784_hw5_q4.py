from ArrayStack import *
 
class Queue:
    def __init__(self):
        self.in_stack = ArrayStack()    
        self.out_stack = ArrayStack()   
 
    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)
 
    def is_empty(self):
        return len(self) == 0
 
    def enqueue(self, e):
        self.in_stack.push(e)
 
    def move_if_needed(self):
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
 
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        self.move_if_needed()
        return self.out_stack.pop()
 
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        self.move_if_needed()
        return self.out_stack.top()