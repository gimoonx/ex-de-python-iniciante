def soma(a, b, c, tam):
    for i in range(0, tam):
        c.append(a[i] + b[i])
        
    return c

tam = int(input("Digite o tamanho do vetor: "))
x = [ ]
y = [ ]
z = [ ]

for i in range(tam):
    x.append(int(input("Digite um número x: ")))

for i in range(tam):
    y.append(int(input("Digite um número y: ")))

z = soma(x, y, z, tam)

print("\n", x, "\n", y, "\n", "\n", z)