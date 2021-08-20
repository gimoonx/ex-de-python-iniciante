n= int(input("x²:	"))
r= int(input("x:	"))
l= int(input("numero:	"))

da=(r*r)-(4*n*l)
if da<0:
	x=(-r+(da**1/2))/(2*n)
	yi=(-r-(da**1/2))/(2*n)
	print (x , "+" , yi)

else:
	x1=(-r+(da**1/2))/(2*n)
	x2=(-r-(da**1/2))/(2*n)
	print (x1 , x2)