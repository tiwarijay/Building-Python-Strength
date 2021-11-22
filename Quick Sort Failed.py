# QUICK SORT
# struggling to write quick sort algorithm. (first time)
"""
Approach:
Step 1: pivot = L[0]
Step 2: Get Left wing, right wing and pivot position
Step 3:

    # Some trash to ignore.
    if len(left) <= 1:
        if len(right) > 1:
            # [_] [pivot] [___________]
            return left + [pivot] + quicksort(L, pivot_position+1, len(temp)-1)
        else:
            # [_] {pivot] [_]
            return left + [pivot] + right
    elif len(right) <= 1:
        # [___________] [pivot] [_]
        return quicksort(L, 0, pivot_position-1) + [pivot] + right
    else:
        # len(left) > 1 or len(right) > 1:
        # [________________] [pivot] [________________]
        return quicksort(L, 0, pivot_position-1) + [pivot] + quicksort(L, pivot_position+1, len(temp)-1)
"""

def lpr(L, start, stop):
    left = []
    right = []

    # initialization
    pivot = L[start]
    for element in L[start:stop+1]:
        if element < pivot:
            # left wing
            left.append(element)
        elif element > pivot:
            # right wing
            right.append(element)
        else:
            pass
            # rep.append(element)
            # repetition is ignored for the time being.
    print('partition:',left, pivot, right)
    # left and right wings obtained

    return left, pivot, right

"""
sortedlist = [0]*len(L)
"""
def quicksort(L, start, stop):
    left, pivot, right = lpr(L, start, stop)
    temp = left + [pivot] + right

    pivot_position = len(left)
    L[start:stop+1] = temp
    print('--->:', L)
    print('\n')

    if len(left) <= 1:
        return temp
    if len(right) <= 1:
        return temp
    if len(left) > 1 or len(right) > 1:
        return quicksort(L, 0, pivot_position-1) + [pivot] + quicksort(L, pivot_position+1, len(temp)-1)

#L = [21, 62, 42, 8, 15, 47, 6, 7, 12, 2, 65, 72]

import random
L = [random.randint(0, 100) for i in range(10)]
print(f'L = {L}\n')
quicksort(L, 0, len(L)-1)