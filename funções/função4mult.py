def pro(a , b):
	r=0
	while b>0:
		r=r+a
		b= b-1
	return r
	
a=int(input("digite um numero:	"))
b=int(input("digite outro:	"))

print(pro(a , b))