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
    
