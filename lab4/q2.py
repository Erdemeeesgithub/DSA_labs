def find_pivot(lst):
    if len(lst) == 0:
        return None
    low, high = 0, len(lst) - 1
    while low < high:
        mid = (low + high) // 2
        if lst[mid] > lst[high]:   
            low = mid + 1
        else:                    
            high = mid
    return low
 
 
def binary_search(lst, target, low, high):
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None
 
 
def shift_binary_search(lst, target):
    if len(lst) == 0:
        return None
    p = find_pivot(lst)
    if lst[p] <= target <= lst[-1]:
        return binary_search(lst, target, p, len(lst) - 1)
    return binary_search(lst, target, 0, p - 1)