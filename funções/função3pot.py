def pot(b , e):
	aux=b
	r=0
	
	while e>1:
		r=aux*b
		aux=r
		e=e-1
		
	return r
	
b=int(input("b:	"))
e=int(input("e:	"))

print(pot(b , e))