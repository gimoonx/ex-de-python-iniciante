def soma_vetores(a,b,c,t):
    
    for i in range(t):
        a.append(int(input('a: ')))

    for i in range(t):
        b.append(int(input('b: ')))

    for i in range(0,t): #0,1,2,3,4
        c[i] = a[i] + b[i]

    print(c)

###################
    
t = int(input('Quant. elementos: '))

x = []
y = []
z = t*[0]

soma_vetores(x,y,z,t)