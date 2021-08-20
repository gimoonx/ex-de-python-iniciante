def primo(n):
	i=1
	cont=0
	
	while i<=n:
		if n%i ==0:
			cont=cont+1
			
		i=i+1
		
	if cont ==2:
		return True
			
	else:
		return False
			
n=int(input("digite um numero:	"))
print (primo(n))