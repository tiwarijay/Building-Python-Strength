# SEARCH 0 IN A LIST RECURSIVELY
""" This is a piece of code to check if a given list has 0 in it or not. If it has "zero" in it, we return true(1),
otherwise we return false(0). """

def check0(L):
    # if the list is empty, return False
    if len(L) == 0:
        return 0
    # if the list is not empty, then check...
    # whether the first element in the list is zero or not.
    if L[0] == 0:
        # if the first element is zero, then return 1.
        return 1
    else:
        return check0(L[1:len(L)])
        # the above code simply outsources.

print(check0([1,2,4,5,10,7,8,3]))

# Please note: This is not an efficient code, we will see this later.
# This introduces the concept of recursion.
