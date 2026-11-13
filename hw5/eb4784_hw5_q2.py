from ArrayStack import *
 
class MaxStack:
    def __init__(self):
        self.data = ArrayStack() 
 
    def __len__(self):
        return len(self.data)
 
    def is_empty(self):
        return len(self) == 0
 
    def push(self, e):
        if self.is_empty():
            self.data.push((e, e))
        else:
            cur_max = self.data.top()[1]
            if e > cur_max:
                cur_max = e
            self.data.push((e, cur_max))
 
    def top(self):
        if self.is_empty():
            raise Exception("MaxStack is empty")
        return self.data.top()[0]
 
    def pop(self):
        if self.is_empty():
            raise Exception("MaxStack is empty")
        return self.data.pop()[0]
 
    def max(self):
        if self.is_empty():
            raise Exception("MaxStack is empty")
        return self.data.top()[1]