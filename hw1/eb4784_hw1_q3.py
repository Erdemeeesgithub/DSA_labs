def sum_squares(n):
    total = 0
    for i in range(1, n):
        total += i * i
    return total

def sum_odd_squares(n):
    total = 0
    for i in range(1, n, 2):
        total += i * i
    return total

def main():
    n = 5
    print(sum([i * i for i in range(1, n)]))      
    print(sum([i * i for i in range(1, n, 2)])) 