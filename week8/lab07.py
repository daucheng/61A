""" Lab 07: Recursive Objects """

# Q3
def link_to_list(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    "*** YOUR CODE HERE ***"
    """
    #Recursion
    if link is Link.empty:
        return []
    else:
        return [link.first] + link_to_list(link.rest)
    """
    #iterative    
    lst = [link.first]
    while link.rest is not Link.empty:
        link = link.rest
        lst.append(link.first)
    return lst
        

# Q4
def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    """
    "*** YOUR CODE HERE ***"
    #Recursion
    if n == 0:
        return Link.empty
    n = str(n)
    if len(n) == 1:
        return Link(int(n))
    else:
        first,rest = n[0],n[1:]
        return Link(int(first),store_digits(rest))

    """
    #iterative
    s = Link.empty
    while n > 0:
        n , lst = n//10 , n%10
        s = Link(lst,s)
    return s
    """


# Q5
def cumulative_sum(t):
    """Mutates t where each node's root becomes the sum of all entries in the
    corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(t)
    >>> t
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    """
    "*** YOUR CODE HERE ***"
    
    for b in t.branches:
        cumulative_sum(b)
    t.label += sum([b.label for b in t.branches])





# Linked List Class


# Tree Class
class Tree:
    def __init__(self, label, branches=[]):
        for c in branches:
            assert isinstance(c, Tree)
        self.label = label
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.label, branches_str)

    def is_leaf(self):
        return not self.branches

    def __eq__(self, other):
        return type(other) is type(self) and self.label == other.label \
               and self.branches == other.branches
    
    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

    def copy_tree(self):
        return Tree(self.label, [b.copy_tree() for b in self.branches])