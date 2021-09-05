mat = [[1,0,1],[1,1,0],[1,1,0]]
from itertools import product
print(sum([sum(row) for row in mat]))
n = len(mat)
m = len(mat[0])
for i, j in product(range(1, n+1),range(1, m+1)):
    if i*j == 1:
        continue
    for k,l in product(range(n-i+1),range(m-j+1)):
        print([row[l:l+j] for row in mat[k:k+i]])
