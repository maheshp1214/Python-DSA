"""Simple Recursion based problems"""

def N(n):
    if n>0:
        N(n-1)
        print(n,end=' ')
def N_reverse(n):
    if n>0:
        print(n,end=' ')
        N_reverse(n-1)
def N_odd(n):
    if n>0:
       N_odd(n-1)
       print(2*n-1,end=' ')
def N_even(n):
    if n>0:
        N_even(n-1)
        print(2*n,end=' ')
def N_odd_reverse(n):
    if n>0:
        print(2*n-1,end=' ')
        N_odd_reverse(n-1) 
def N_even_reverse(n):
    if n>0:
        print(2*n,end=' ')
        N_even_reverse(n-1) 
def N_sum(n):
    if n==1:
        return 1
    n1= n + N_sum(n-1)   
    return n1
def N_odd_sum(n):
    if n==1:
        return 1
    return 2*n-1 + N_odd_sum(n-1)
def N_even_sum(n):
    if n==1:
        return 2
    return 2*n + N_even_sum(n-1)
def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)
def N_square_sum(n):
    if n==1:
        return 1
    return n*n + N_square_sum(n-1)

# N(10)
# N_reverse(10)
# N_odd(10)
# N_even(10)
# N_odd_reverse(10)
# N_even_reverse(10)
# print(N_sum(10))
# print(N_odd_sum(10))
# print(N_even_sum(10))
# print(factorial(5))
# print(N_square_sum(3))