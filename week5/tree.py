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
def tree(label, branches=[]): #by default the list of branches is empty = a leaf
    for branch in branches:
        assert is_tree(branch) #varifies the tree definition
    return [label] + branches #creates a list for a sequence  of branches

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