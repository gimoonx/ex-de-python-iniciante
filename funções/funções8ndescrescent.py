def nd(n):
	aux=0
	aux2=0
	
	while n>0:
		aux= n%10
		n= n//10
		aux2= n%10
		
		if aux2>aux:
			return False
			break
			
		if n==0:
			return True
			
n=int(input("digite um numero:	"))

print(nd(n))