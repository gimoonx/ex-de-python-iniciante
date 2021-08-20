n=int(input("digite o numero de elementos:	"))
#variáveis definidas que ajudarão no while
i=0
soma=0

while i<n:
	y=int(input("digite:	"))
	soma=soma+y
#ex:1° n digitado › 2+y(proximo número digitado)
#nisso fica soma=2+3 (ex)
#soma=5 (prossegue se tiver mais elementos)
	i=i+1
#vai rodando a qntd de elementos
print("soma total" , soma)

#não é necessário no exercício
print("quantidade de elementos" , i)