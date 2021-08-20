a= float(input('insira um numero real:	'))
b= float(input('insira outro numero real:	'))
c= float(input('insira mais um numero real:	'))

if a>b and a>c:
	print ('numero maior' , a)
elif b>c and b>a:
	print ('numero maior' , b)
else:
	print ('numero maior' , c)