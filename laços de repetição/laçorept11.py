soma=0
i=0
while True:
	y=int(input("digite um numero:	"))
	soma=soma+y
	i=i+1
	if y==0 and i>1:
		break
		
print("total" , soma)