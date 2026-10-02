def factors(num):
    i = 1
    while i * i < num:          
        if num % i == 0:
            yield i
        i += 1

    if i * i == num:            
        yield i

    i -= 1
    while i >= 1:              
        if num % i == 0:
            yield num // i
        i -= 1