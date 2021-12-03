# BINARY SEARCH

# Let's start by searching in the trivial way...
def obvious_search(L, k):
    """
    Searching the element 'k' in the list L by comparing all elements of list with our k.
    """
    for x in L:
        if x == k:
            # found
            return 1
    # We are out of for loop.
    # which means, k not found.
    return 0
# ------------------------------------------------------------------------------------------------------------------

# Now let's try implementing the amazing binary search using first principles...
def binary_search_fp(L,k):
    """
    Here were are considering that our list L is already sorted.
    We take the element at the middle index of the list as our pivot element, compare it with our k, and then discard
    half of the list L.
    """
    begin = 0
    end = len(L)-1


    while (end - begin > 0):
        # if there are at least 2 elements...then, repeat.

        mid = (begin + end)//2
        # integral part here will be our middle index.

        if k == L[mid]:
            # We got our element.
            return 1
        elif k < L[mid]:
            # Our desired element must be in the left half, if it is present at all.
            # So, retain left half and discard right half.
            end = mid - 1
        else:
            # k > L[mid]
            # retain right half.
            begin = mid + 1

    # If we reach here, it means we haven't found out element yet and now end = begin. We have only one element.
    if L[begin] == k:
        return 1
    else:
        return 0
        # element not found.

# ----------------------------------------------------------------------------------------------------------------

# BINARY SEARCH USING RECURSION
def binary_search_rec(L, k, begin, end):
    """
    Let's implement the binary search using recursion.
    """

    if end-begin == 0:
        # list L has only one element
        if L[begin] == k:
            return 1
        return 0
        # List got only one element, k not found
    elif end-begin < 0:
        return 0
        # not found
    else:
        # we still have some elements to check
        mid = (begin + end)//2
        # for pivot

        if k == L[mid]:
            return 1
            # k is present in the list L.
        elif k < L[mid]:
            # k must be in left wing
            return binary_search_rec(L, k, begin, mid-1)
        elif k > L[mid]:
            # k must be in right wing
            return binary_search_rec(L, k, mid+1, end)
        else:
            return 0
            # k not found
# #---------------------------------------------------------------------------------

# Testing the code.
import time
L = list(range(10**8))
# print(L)
k = 10**8 - 1
# to search

a = time.time()
print(obvious_search(L, k))
b = time.time()
print(f'Obvious search took {b-a} secs')

print(binary_search_fp(L, k))
c = time.time()
print(f'Obvious search using first principles took {c-b} secs')

print(binary_search_rec(L, k, 0, len(L)-1))
d = time.time()
print(f'Binary search using recursion took {d-c} secs')





