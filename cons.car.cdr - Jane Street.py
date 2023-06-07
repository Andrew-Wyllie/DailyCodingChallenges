def cons(a, b):
    return (a, b)

def car(x):
    return x[0]

def cdr(x):
    return x[1]

output1 = car(cons(3, 4))
output2 = cdr(cons(3, 4))

print("car result = ", output1)
print("cdr result = ", output2)



