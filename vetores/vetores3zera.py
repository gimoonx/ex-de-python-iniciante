#zera os pares do vetor

def zera(a, tam):
    for i in range(tam):
        if a[i] % 2 == 0:
            a[i] = 0

    return a

tam = int(input("Digite um tamanho de vetor: "))
a = [ ]

 i in range(tam):
    a.append(int(input("Digite um número a: ")))

a = zera(a, tam)

print(a)