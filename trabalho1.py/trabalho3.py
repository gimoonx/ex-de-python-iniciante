n=int(input("Digite o número: "))

p=0
p=p+1*(n%2)
d=0
      

while n>0:
    n=n//10
    p=p+1*(n%2)
    d=d+1

p=d-p

print("Dígitos pares:" ,p)