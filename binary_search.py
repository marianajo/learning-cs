def binary_search(l, item):
    
    low = 0
    high = len(l) - 1

    while low <= high:
        half = (low + high) // 2
        guess = l[half]

        if guess == item:
            return half
        if guess > item:
            high = half - 1
        else:
            low = half + 1
    return None


l = [1, 3, 5, 7, 9]
print(binary_search(l, 7))


