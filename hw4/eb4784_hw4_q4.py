def list_min(lst, low, high):
    if low == high:
        return lst[low]
    rest_min = list_min(lst, low + 1, high)  
    if lst[low] < rest_min:
        return lst[low]
    return rest_min

