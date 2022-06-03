from decimal import *
def float_sum(A, B):
    x = max([len(str(A)[str(A).index(".")+1:]), len(str(B)[str(B).index(".")+1:])])
    print(x)
    return format(A + B, "."+str(x)+"f")

a = float_sum(99.1, 0.109)
print(a)