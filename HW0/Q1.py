import numpy as np

A = []
B = []

with open('matrixA.txt','r') as fa:
    for line in fa.readlines():
#        for x in line.split(','):
#            A.append((int)x)
        row = [int(x) for x in line.split(',')]
        A.append(row)

with open('matrixB.txt','r') as fb:
    for line in fb.readlines():
#        for x in line.split(','):
#            B.append((int)x)
        row = [int(x) for x in line.split(',')]
        B.append(row)

#print(A)
#print(B)

A = np.array(A)
B = np.array(B)

result = A.dot(B)
result.sort(axis=1)

np.savetxt("ans_one.txt", result, fmt="%d", delimiter="\r\n")

#print(result)
