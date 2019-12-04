def xk(c,d):
    if c==4:
        return 6
    elif d>=4:
        return 6+7+c
    else:
        return 25
def sobig(x):
    if x>10:
        print('huge')
    elif x>5:
        return 'big'
    elif x>0:
        print('small')
    else:
        print("nothin")

def bake(cake, make):
     if cake == 0:
         cake = cake + 1
         print(cake)
     if cake == 1:
         print(make)
     else:
         return cake
     return make            
