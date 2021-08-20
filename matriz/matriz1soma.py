def soma(a,b,m,n):
    c = [[0 for C in range(n)] for L in range(m)]
    for lin in range(m):
        for col in range(n):
            c[lin][col] = a[lin][col] + b[lin][col]
    return c

def levalor(a,linha,coluna):
    for i in range(linha): #contar linhas de A:
        for j in range(coluna): #contar colunas de A:
            a[i][j] = int(input('[%d][%d]: ' %(i,j)))
        print('')

def exibe_matriz(a,linha,coluna):
    #exibir matriz:
    for i in range(linha):
        for j in range(coluna):
            print('%d ' %(a[i][j]), end='')
        print('')

#####################
LIN = 3
COL = 3

a = [[0 for i in range(COL)] for j in range(LIN)]
b = [[0 for i in range(COL)] for j in range(LIN)]

levalor(a,LIN,COL)
levalor(b,LIN,COL)

c = soma(a,b,LIN,COL)

exibe_matriz(c,LIN,COL)