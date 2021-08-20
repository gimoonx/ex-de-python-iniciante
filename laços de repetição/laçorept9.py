n=int(input("qntd de elementos:	"))
i=0
soma=0

#soma de pares apenas

while i<n:
	y=int(input("digite:	"))
	if y%2==0:
	#SE y(numero digitado) for divisivel por 2
	#ou seja, vai dar resultado 0
		soma=soma+y
		#soma será feita (soma=0+y)
		#armazena o y
	i=i+1
	#qntd de elementos
print("soma dos pares" , soma)