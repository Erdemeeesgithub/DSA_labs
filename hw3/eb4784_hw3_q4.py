def remove_all(lst, value):
    write = 0
    for read in range(len(lst)):
        if lst[read] != value:
            lst[write] = lst[read]
            write += 1
    while len(lst) > write:
        lst.pop()