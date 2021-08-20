def cop(a, b, tam):
	for i in range(tam):
		b=a
		
	return b
	
tam=int(input("digite o tamanho do vetor:	"))
a=[ ]
b=[ ]

for i in range(tam):
	a.append(int(input("digite um numero a:	")))

#(adicona valor em b)
#for i in range(tam):
	#b.append(int(input("digite um numero b:	")))

b=cop(a, b, tam)

print(a)
print(b)