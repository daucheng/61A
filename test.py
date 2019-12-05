def repeat(f,x):
    while f(x) !=x:
        x = f(x)
    return x

def g(y):
    return(y+5)//3

def make_adder(n):
        def adder(k):
            return k+n
        return adder

def square(x):
        return x*x
def triple(x):
        return 3*x
def compose(f,g):
    def h(x):
        return f(g(x))
    return h
