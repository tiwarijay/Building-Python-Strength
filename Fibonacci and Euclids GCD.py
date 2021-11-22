# GCD and FIBONACI
import time
def gcd(a, b):
    """
    Gives GCD of two numbers a and b using Euclid's Algorithm..
    """
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
# gcd() tested and verified.

# FIBONACCI :to use as arguments in GCD to check time complexity.
def fib(n):
    '''
    Gives nth element in the fibonacci sequence.
    '''

    if n < 1:
        print('Invalid input. Enter a positive integer.')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
# fib() tested and verified.

import time
t3 = time.time()
a = fib(100)
t4 = time.time()
b = fib(99)
t5 = time.time()
print(f'Time taken to get fibonacci: {t4 - t3:.8f}s and {t5 - t4:.8f}s')


t1 = time.time()
print(f'GCD({a},{b}) = {gcd(a,b)}')
t2 = time.time()
print(f'Time taken to get GCD: {t2 - t1:.8f}s')
# Gives time taken to compute GCD of two large fibonacci numbers.

