def identidade(a,m,n):

    c = 0
    for i in range(m):
        for j in range(n):
            if a[i]== a[j]and a[i][j]==1:
                 c = c + 1 

    if c == 4:
        return True
    else:
        return False 
            
LIN = 4
COL = 4

a = [[0 for i in range(COL)] for j in range(LIN)]

for i in range(LIN):
    for j in range(COL):
        a[i][j] = int(input('A: [%d][%d]' %(i,j)))
    

# 10 10 10 10 -> A[0][0]
# 10 10 10 10 -> A[1][1]
# 10 10 10 10 -> A[2][2]
# 10 10 10 10 -> A[3][3]

print(identidade(a,LIN,COL))