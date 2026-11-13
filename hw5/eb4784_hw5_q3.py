from ArrayStack import *
from ArrayDeque import *
 
class MidStack:
    def __init__(self):
        self.bottom = ArrayStack()
        self.upper = ArrayDeque()
 
    def __len__(self):
        return len(self.bottom) + len(self.upper)
 
    def is_empty(self):
        return len(self) == 0
 
    def balance(self):
        target = (len(self) + 1) // 2
        if len(self.bottom) > target:
            self.upper.enqueue_first(self.bottom.pop())
        elif len(self.bottom) < target:
            self.bottom.push(self.upper.dequeue_first())
 
    def push(self, e):
        self.upper.enqueue_last(e)
        self.balance()
 
    def top(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        if self.upper.is_empty():
            return self.bottom.top()
        return self.upper.last()
 
    def pop(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        if self.upper.is_empty():
            value = self.bottom.pop()
        else:
            value = self.upper.dequeue_last()
        self.balance()
        return value
 
    def mid_push(self, e):
        self.bottom.push(e)
        self.balance()