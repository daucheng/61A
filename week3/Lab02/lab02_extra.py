""" Optional problems for lab02 """

from lab02 import *

# Higher Order Functions

def compose1(f, g):
    """Return the composition function which given x, computes f(g(x)).

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> a1 = compose1(square, add_one)   # (x + 1)^2
    >>> a1(4)
    25
    >>> mul_three = lambda x: x * 3      # multiplies 3 to x
    >>> a2 = compose1(mul_three, a1)    # ((x + 1)^2) * 3
    >>> a2(4)
    75
    >>> a2(5)
    108
    """
    return lambda x: f(g(x))

def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2, 
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1)^2 == 0^2 + 1
    True
    >>> b1(4)                            # (4 + 1)^2 != 4^2 + 1
    False
    """
    "*** YOUR CODE HERE ***"
    def test_identity(x):
        if compose1(f,g)(x) == compose1(g,f)(x):
            return True
        else: 
            return False
    
    return test_identity

def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function CONDITION.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"
    def count(n):
        count_true , test_data = 0 , 1
        while test_data <= n:
            if condition(n , test_data):
                count_true = count_true +1
            test_data += 1    
        return count_true                
    return count

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10    
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    """
    
        def take_arg_n(n):
        def take_arg_x(x):
            sum_res,i = x,0
            ori_ls = [f1,f2,f3]
            func_ls = ori_ls*(n//3) + ori_ls[0:n%3]
            if n == 0:
                return x
            else:
                while i<n:
                    sum_res = func_ls[i](sum_res)
                    i +=1
                return sum_res
        return take_arg_x
    return take_arg_n
    """
    def count_cycle(x):
        if x == 0:
            return lambda x:x
        else:
            def count_ans(n):
                circle_num , ans = 1 , n
                while circle_num <= x:
                    if circle_num % 3 == 1:
                        circle_num,ans =circle_num+1, f1(ans)
                    elif circle_num % 3 == 2:
                        circle_num,ans =circle_num+1, f2(ans)
                    else:
                        circle_num,ans =circle_num+1, f3(ans)
                return ans 
        return count_ans          
    return count_cycle
