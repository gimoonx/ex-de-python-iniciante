def junta_valores(a,b,c,tam1,tam2):
    
    for i in range(tam1):
        a.append(int(input('A: ')))
    

    for i in range(tam2):
        b.append(int(input('B: ')))
    

    c = a + b
    return (tam1+tam2)

#####return guarda o valor no def########

t1 = int(input('Tamanho de A: '))
t2 = int(input('Tamanho de B: '))

x = []
y = []
z = []

print(junta_valores(x,y,z,t1,t2))