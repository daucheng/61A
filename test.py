def create_row(size):
    """Returns a single, empty row with the given size. Each empty spot is
    represented by the string '-'.

    >>> create_row(5)
    ['-', '-', '-', '-', '-']
    """
    "*** YOUR CODE HERE ***"
    row_num = ['_']
    def row(count):
        if count == 1:
            return row_num
        else:
            count = count -1
            row_num.append('_')
            return row(count) 

    return row(size)

def accumulate(lst):
    count = 0 
    for i in range(len(lst)):
        item = lst[i]
        if isinstance(item,list):
            inside = accumulate(item)
            count += inside
        else:            
            count += item
            lst[i] = count
    return count 
            
"""
def a(lst):
    sum_so_far = 0
    for i in range(len(lst)):
        item = lst[i]
        if isinstance(item, list):
            inside = accumulate(item)
            sum_so_far += inside
        else:
            sum_so_far += item
            lst[i] = sum_so_far
    return sum_so_far
"""
