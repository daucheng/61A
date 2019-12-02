"""def lf(n):
   for i in range(n-1,0,-1):
       if n % i ==0:
           return i
           
"""
def lf(n):
    factor = []
    i = 1
    while i < n-1:
        if n % i ==0:
            factor.append(i)
        i += 1
    print(max(factor))

#if_statement 當c()為true時 直接return c() 與else內無關 不會check even it's wrong
def if_function(condition, true_result, false_result):
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    if c():
        return t()
    else:
        return f()
#當寫在if_function內時 會先check every operand 因此f()的錯誤會導致 無法執行
def with_if_function():
    return if_function(c(), t(), f())

def c():
    return True

def t():
    return i
    
def f():
    abc
