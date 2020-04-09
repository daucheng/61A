class Link:
    empty = ()
    def __init__(self, first, rest = empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __getitem__(self,i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]
    def __len__(self):
            return 1 + len(self.rest)

    def link_expression(s):
        """Return a string that would evaluate to s."""
        if s.rest is Link.empty:
            rest = ''
        else:
            rest = ', ' + link_expression(s.rest)
        return 'Link({0}{1})'.format(s.first, rest)
def sum_nums(lnk):
    sum = 0
    while lnk:
        if lnk.rest == Link.empty:
            sum += lnk.first
            return lnk
        else:
            sum+= lnk.first
            lnk = lnk.rest
