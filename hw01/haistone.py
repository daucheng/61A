def hailstone(n):
    hail = []
    b = n
    hail.append(b)
    while b != 1:
        if b % 2 == 0:
            b = b/2
            hail.append(int(b))        
        else:
            b = (3*b)+1
            hail.append(int(b))
    print(hail)
    return len(hail)
        
