def find_duplicates(lst):
    n = len(lst)
    counts = [0] * n
    result = []
    for val in lst:
        counts[val] += 1
        if counts[val] == 2:
            result.append(val)
    return result