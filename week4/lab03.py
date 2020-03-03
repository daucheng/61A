##GCD

def gcd(a,b):
    if a%b == 0:
        return b
    elif a%b == 1:
        return 1
    return gcd(b, a%b)
    
##Hailstone


def hailstone(n):
   
    if n == 1:
        return 1
    elif n%2 == 0:
        print(n)
        return hailstone(n//2)
    else:        
        print(n)
        return hailstone(n*3+1)
