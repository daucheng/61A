def product(m,n):
    if n == 1:
        return m
    else:
        return m + product(m,n-1)

def countdown(n):
    if n == 1:
        print("1")
    else:
        print(n)
        return countdown(n-1)
def countup(n):
    if n == 1:
        print(1)
    else:
        countup(n-1)
        print(n)

def sum_digits(n):
    if n // 10 == 0:
        return n
    else:
        return (n%10) + sum_digits(n//10)
"""
def count_stair_ways(n):
    count = 0
    if n - 2 == 0:
        count = count + 2
    elif n -1 == 0:
        count = count + 1
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)
    return count
"""
def count_stair_ways(n):
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)
def count_k(n,k):
    if n == 0: #valid step
        return 1
    if n < 0: #invalid step
        return 0
    i , total = 1 , 0
    while i <= k:
        total += count_k(n-i,k)
        i += 1
    return total
        
