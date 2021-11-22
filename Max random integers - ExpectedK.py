# Selecting l random numbers between 1 to N and getting the expected value of the element at kth position in the sorted list.

import random
def expectedk(N, l, k, iter):
    """
    N = upper range of random integer
    l = number of random elements to pick
    k = (position of) element of which we want the expected value
    iter = Number to iterations to take average from.

    Returns two answers.
    Empirical, after performing iteration.
    Intuition based on equi-partition idea.
    """
    sum=0
    for j in range(iter):
      L=[]
      for i in range(l):
        L.append(random.randint(1,N))
      S = sorted(L)
      sum = sum + S[k-1]

    print(f" {l} random integers taken between 1 to {N}.")
    print(f"We want the expected value of the element at {k}th position out of {l} numbers. ")
    return print(f"Empirical answer after {iter} iterations: {sum/iter}. \nIntuition: {k * (N/(l+1))}")

expectedk(1000, 15, 1,10**5)
