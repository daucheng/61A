class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
#To check if a Link is empty, compare it against the class attribute Link.empty:
if link is Link.empty:
    print('This linked list is empty!')

def skip(lst):

    if lst == Link.empty:
        return Link.empty
    elif lst.rest == Link.empty:
        return Link(lst.first)
    return Link(lst.first,skip(lst.rest.rest))

def reverse(lst):
#Iterative
    rev = Link.empty
    while lst is not Link.empty:
        rev = Link(lst.first,rev)
        lst = lst.rest
    return rev
"""
#Recursive
    def helper(so_far,rest):
        if rest is link.empty:
            return so_far
        else:
            return helper(Link(rest.first,so_far),rest.rest)
    return helper(Link.empty, lst)
"""
class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = branches
    def is_leaf(self):
        return not self.branches

def contains_n(elem, n, t):
    if n == 0:
        return True
    elif t.is_leaf():
        return n == 1 and t.label == elem 
    elif t.label == elem:
        return True in [contains_n(elem,n-1,b) for b in t.branches]
    else:
        return True in [contains_n(elem,n,b) for b in t.branches] 

def factor_tree(n):
    for i in range(2,n) :
        if n % i == 0:
            return Tree(n,[i,factor_tree(n//i)])
    return Tree(n)