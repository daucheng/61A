def tree(label, branches=[]): #by default the list of branches is empty = a leaf
    for branch in branches:
        assert is_tree(branch) #varifies the tree definition
    return [label] + branches #creates a list for a sequence  of branches
#selector
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:] 

def is_tree(tree):
    if type(tree) != list or len(tree) < 1: #verifies that tree is bound to a  list
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True
def is_leaf(tree):
    return not branches(tree)

def sum_range(t):
    """Returns the range of the sums of t, that is, the
difference between the largest and the smallest
sums of t."""
    def helper(t):
        if is_leaf(t):
            return [label(t), label(t)]
        else:
            a = min([label(helper(b)) for b in branches(t)])
            b = max([label(helper(b)) for b in branches(t)])
            x = label(t)
            return [b+x,a+x]                
    x, y = helper(t)
    return x - y
"""
t = tree(5,[tree(1,[tree(7,[tree(4,[tree(3)])])
                ,tree(2)])
        ,tree(2,[tree(0),tree(9)])])
"""
def no_eleven(n):
    """Return a list of lists of 1's and 6's that do not
    contain 1 after 1.
    >>> no_eleven(2)
    [[6, 6], [6, 1], [1, 6]]
    >>> no_eleven(3)
    [[6, 6, 6], [6, 6, 1], [6, 1, 6], [1, 6, 6], [1, 6, 1]]
    >>> no_eleven(4)[:4] # first half
    [[6, 6, 6, 6], [6, 6, 6, 1], [6, 6, 1, 6], [6, 1, 6, 6]]
    >>> no_eleven(4)[4:] # second half
    [[6, 1, 6, 1], [1, 6, 6, 6], [1, 6, 6, 1], [1, 6, 1, 6]]
    """
    if n == 0:
        return [[]]
    elif n == 1:
        return [[6],[1]]
    else:
        a, b = no_eleven(n-1), no_eleven(n-2)
    return [ [6]+s for s in a] + [[1,6]+s for s in b]

def eval_with_add(t):
    """Evaluate an expression tree of * and + using only
    addition.
    >>> plus = Tree('+', [Tree(2), Tree(3)])
    >>> eval_with_add(plus)
    5
    >>> times = Tree('*', [Tree(2), Tree(3)])
    >>> eval_with_add(times)
    6
    >>> deep = Tree('*', [Tree(2), plus, times])
    >>> eval_with_add(deep)
    60
    >>> eval_with_add(Tree('*'))
    1
    """
    if label(t) == '+':
        return sum([eval_with_add(b) for b in branches(t)])
    elif label(t) == '*':
        total = 1
        for b in branches(t):
            total, term = 0, total
            for _ in  range(eval_with_add(b)):
                total = total + term
        return total
    else:
        return label(t)




