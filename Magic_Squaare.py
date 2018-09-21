import numpy as np

N=input("Enter a number: ")
O=int(N)
magic_square = np.zeros((O,O), dtype=int)

n = 1
i, j = 0, O//2

while n <= O**2:
    magic_square[i, j] = n
    n += 1
    newi, newj = (i-1) % O, (j+1)% O
    if magic_square[newi, newj]:
        i += 1
    else:
        i, j = newi, newj

print(magic_square)

print("Sum of each row/column/diagonal is : ",O*(O**2+1)/2)
