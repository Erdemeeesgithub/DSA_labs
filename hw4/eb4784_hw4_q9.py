def permutations(lst, low, high):
    if low == high:
        return [[lst[low]]]
    smaller = permutations(lst, low, high - 1)
    result = []
    for p in smaller:
        for i in range(len(p) + 1):
            result.append(p[:i] + [lst[high]] + p[i:])
    return result