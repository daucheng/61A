def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f,g,n):
    if n:
        f(n)
        g(n)

          
#grow = lambda n: f_then_g(grow, print, n//10)

#shrink = lambda n: f_then_g(print, shrink, n//10)

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
    
