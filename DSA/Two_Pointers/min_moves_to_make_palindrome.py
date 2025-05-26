def min_moves_to_make_palindrome(s):
    move = 0
    l = list(s)
    n = len(l)
    i, j = 0, n-1
    while i < j:
        if l[i] == l[j]:
            i += 1
            j -= 1
        else:
            k = j
            while k > i and l[k] != l[i]:
                k -= 1
            if k == i:
                l[i], l[i+1] = l[i+1], l[i]
                move += 1
            else:
                while k < j:
                    l[k], l[k+1] = l[k+1], l[k]
                    k += 1
                    move += 1
                i += 1
                j -= 1
    return move
