# calculate d for the list of numbers using the given formula
c = 50
h = 30
# use the formula Q = square root of [(2*c*d)/h]
#find d

import math
x = []
y = [i for i in input('Give me cs numbers: ').split(',')]
for d in y:
    x.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print(','.join(x))