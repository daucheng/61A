#3
def fox_says(start, middle, end, num):
    def repeat(num):
        if num == 1:
            return middle
        else:
            return middle +'-' + repeat(num-1)
    return start + "-" + repeat(num) + "-" + end
"""
Fill in the blanks (without using any numbers in the first blank)
such that the entire expression evaluates to 9.
(lambda x: lambda y: ________________)(_____)(lambda z: z*z)()
"""
 #(lambda x: lambda y: lambda: y(x))(3)(lambda z: z*z)()
"""
(lambda x : ...)(3) >>> x=3 return func y
(lambda y : ...)(lambda z: z*z) >>> func y=lambda z return lambda
(lambda :y(x))() >>>
z=3 lambda z:z*z return 9
(lambda :y(x))() return 9

"""
#4
def combine(n,f,result):
    if n == 0:
        return result
    else:
        return combine(n//10,f,f(n%10,result))

#5
def has_sum(total,n,m):
    if total == 0:
        return True
    elif total < 0:
        return False
    return has_sum(total-n,n,m)or has_sum(total-m,n,m)
#6
def sum_range(lower,upper):
    def copies(pmin,pmax):
        if pmin >= lower and pmax <= upper:
            return True
        elif pmax > upper:
            return False
        return copies(pmin+50,pmax+60) or copies(pmin+130,pmax+140)
    return copies(0,0)

