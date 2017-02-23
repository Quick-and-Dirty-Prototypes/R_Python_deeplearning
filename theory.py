import numpy as np

def AND(x1,x2):
    x = np.array(x1 , x2)
    w = np.array(0.5 , 0.5)
    b = -0.7
    tmp = sum(w*x+b)
    if tmp>=0:
        return 1
    else:
        return 0

# def OR(x1,x2):


# def XOR(x,y)
#    s1 = NAND
