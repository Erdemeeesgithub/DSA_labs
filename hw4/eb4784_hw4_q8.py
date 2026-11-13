def flat_list(nested_lst, low, high):
    if low > high:
        return []
    first = nested_lst[low]
    if isinstance(first, list):
        result = flat_list(first, 0, len(first) - 1)
    else:
        result = [first]
    result.extend(flat_list(nested_lst, low + 1, high))
    return result