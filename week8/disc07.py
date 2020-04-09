class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.second
    3
    >>> s.first = 5
    >>> s.second = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value


    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

def sum_nums(lnk):
    sum = 0
    while lnk:
        if lnk.first == Link.empty:
            pass
        else:
            sum += lnk.first
        lnk = lnk.rest
    return sum

def multiply_lnks(lst_of_lnks):
    assert len(lst_of_lnks) > 0, 'lst of lnks contains at least one linked list'

    product = 1
    
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return Link.empty
        product *= lnk.first
    lst_of_lnks_rest = [lnk.rest for lnk in lst_of_lnks]
    return Link(product,multiply_lnks(lst_of_lnks_rest))

#Iterative solution:
"""
    import operator
    from functools import reduce
    def prod(factors):
        return reduce(operator.mul, factors, 1)
    head = Link.empty
    tail = head
    while  Link.empty is not in lst_of_lnks:
        all_prod = prod([a.first for a in lst_of_lnks])
        if head is Link.empty: #first of the new linked list
            head = Link(all_prod)
            tail = head
        else:
            tail.rest = Link(all_prod)
            tail = tail.rest
        lst_of_lnks = [l.rest for l in lst_of_lnks]
    return head
"""
def remove_duplicates(lnk):
    
    if lnk.rest == Link.empty:
        return
    if lnk.first == lnk.rest.first:
        lnk.rest = lnk.rest.rest
        remove_duplicates(lnk)
    else:
        remove_duplicates(lnk.rest)
    """
    if the ending condition setting: lnk == Link.empty
    than the final iterate is empty so no lnk.first
    come up with the error 'tuple' object has no attribute 'first'
    """ 
def even_weighted(lst):
    return [i * lst[i] for i in range(len(lst)) if i%2 == 0]
def quicksort_list(lst):
    if not lst or len(lst) == 1:
        return lst
    pivot = lst[0]
    less = [i for i in lst if i < pivot]
    greater = [i for i in lst if i > pivot]
    return quicksort_list(less)+[pivot]+quicksort_list(greater)
def max_product(lst):
    
    if len(lst) == 0:
        return 1
    elif len(lst) == 1:
        return lst[0]
    else:
        max(max_product(lst[1:]), lst * max_product[2:])

def redundant_map(t, f):
    
    t.label = f(t.label)
    new_f = lambda x: f(f(x))
    for b in t.branches:
        redundant_map(b,new_f)
    