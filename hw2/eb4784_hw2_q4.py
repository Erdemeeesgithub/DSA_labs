def e_approx(n):
    total = 1        
    fact = 1
    for k in range(1, n + 1):
        fact *= k   
        total += 1 / fact
    return total