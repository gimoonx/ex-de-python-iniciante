def tam(n):
	i=0
	
	while n>0:
		i= i+1
		n=n//10
		
	return i
	
n=int(input("digite um numero:	"))

print(tam(n))