def shift(lst, k, direction='left'):
    for i in range(k):
        if direction == 'left':
            lst.append(lst.pop(0))
        elif direction == 'right':
            lst.insert(0, lst.pop())
        
