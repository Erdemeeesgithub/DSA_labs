def reverse_list(lst, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(lst) - 1
        
    while low < high:
        lst[low], high[high] = lst[high], lst[low]
        low += 1
        high -= 1
        
def max_minimums(lst):
    if len(lst) == 0:
        return 
    curr_max = 0
    yield curr_max
    for i in range(1, len(lst)):
        if lst[i] > curr_max:
            curr_max = lst[i]
            yield curr_max
            
def move_zeros(nums):
    zeros = 0 
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[zeros], nums[i] = nums[i], nums[zeros]
            zeros += 1
        

