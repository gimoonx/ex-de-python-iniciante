soma=0

while True:
#enquanto for verdade a sequencia abaixo

	y=int(input("digite um numero:	"))
	soma=soma+y
	#soma os numeros digitados
	if y==0:
	#quando for digitado o numero 0 laço para
		break
		#para o laço seguindo a condição
print("soma total" , soma)