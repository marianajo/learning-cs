def binary_search(l, item):
    """Given an ordered list l and an item, return the item's position 
    on the list. If the item cannot be found on the list, return None.
    """

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
