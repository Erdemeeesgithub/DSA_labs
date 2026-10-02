def findChange(lst01):
    low = 0
    high = len(lst01) - 1
    result = None
    while low <= high:
        mid = (low + high) // 2
        if lst01[mid] == 1:
            result = mid      
            high = mid - 1
        else:
            low = mid + 1      
    return result