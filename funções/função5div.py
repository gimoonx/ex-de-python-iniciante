def div(p , q):
	soma=0
	i=0
	
	while True:
		if p==0:
			i=0
			break
		
		soma=soma+q
		i=i+1
		
		if soma>p:
			soma=soma-q
			i= i-1
			break
			
	return i
	
p=int(input("digite p:	"))
q=int(input("digite q:	"))

print(div(p , q))