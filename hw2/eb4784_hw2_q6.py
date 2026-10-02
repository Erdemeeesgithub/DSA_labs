def two_sum(srt_lst, target):
    left = 0
    right = len(srt_lst) - 1
    while left < right:
        curr = srt_lst[left] + srt_lst[right]
        if curr == target:
            return (left, right)
        elif curr < target:
            left += 1
        else:
            right -= 1
    return None