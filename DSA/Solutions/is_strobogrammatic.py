def is_strobogrammatic(num):
    dict = { '0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    start, end = 0, len(num)-1
    while start < end:
        if num[start] not in dict or dict[num[start]] != num[end]:
            return False
        start += 1
        end -= 1
    return True
