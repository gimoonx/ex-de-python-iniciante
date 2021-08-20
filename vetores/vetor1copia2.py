def copia_vetor(a,b,tam):
    
    #laço para preencher o vetor:
    for i in range(0,tam):
        a[i] = int(input('a: '))

    b = a #copia valor de A.

    print('Vetor A transformado: ', a)   
    print('Vetor B copiado: ', b)

#quantidade dos elementos do vetor:
t = int(input("Insira a quantidade de indices: "))

x = t[0]
y = t[0]

copia_vetor(x,y,t)