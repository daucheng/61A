""" Recursive tree
    root label              
    branch (also a tree)
    leaf : tree with zero branches
    nodes: each location of the tree
"""
#Tree abstraction
"""
>>>tree(3,[tree(1),
           tree(2,[tree(1),
                   tree(1)])])
[3,[1],[2,[1],[1]]]

"""
#constructor
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

def fib_tree(n):
    if n<= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left)+label(right),[left, right])

#return the largest number of the tree
def tree_max(t):
    return max([label(t)]+[tree_max(branch) for branch in branches(t)])

# returns the height of a tree (the longest path from a root to a leaf)
def height(t):
    if is_leaf(t):
        return 0
    return 1 + max([height(b) for b in branches(t)])   

def square_tree(t):
    return tree(label(t)**2,[square_tree(b) for b in branches(t)] )

def find_path(tree ,x):
    if label(tree) == x:
        return [label(tree)] #base case
    paths = [find_path(b,x) for b in branches(tree)]
    for path in paths:
        if path:
            return [label(tree)] +path

def prune(t,k):
    if k == 0:
        return tree(label(t),[])
    else:
        return tree(label(t),[prune(b,k-1) for b in branches(t)])
