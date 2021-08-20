n= int (input('n:	'))
ant=0
atual=1
print(ant,atual)
for i in range (n-2):
	prox=ant+atual
	ant=atual
	atual=prox
	print(prox)