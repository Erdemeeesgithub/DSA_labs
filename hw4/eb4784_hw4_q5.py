def count_lowercase(s, low, high):
    if low == high:
        return 1 if s[low].islower() else 0
    rest = count_lowercase(s, low + 1, high)
    if s[low].islower():
        return rest + 1
    return rest

def is_number_of_lowercase_even(s, low, high):
    if low == high:
        return not s[low].islower()      
    rest_even = is_number_of_lowercase_even(s, low + 1, high)
    if s[low].islower():
        return not rest_even             
    return rest_even