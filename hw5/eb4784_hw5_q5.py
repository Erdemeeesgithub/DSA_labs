from ArrayStack import *
from ArrayQueue import *
 
def permutations(lst):
    s = ArrayStack()      
    q = ArrayQueue()      
    for elem in lst:
        s.push(elem)
    q.enqueue([])
 
    while not s.is_empty():
        elem = s.pop()
        count = len(q)
        for k in range(count):
            perm = q.dequeue()
            for i in range(len(perm) + 1):
                q.enqueue(perm[:i] + [elem] + perm[i:])
 
    result = []
    while not q.is_empty():
        result.append(q.dequeue())
    return result