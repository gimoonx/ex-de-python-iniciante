n= int(input("digite um numero:	"))

if n<=1000 or n<=9999:
	o=n%100
	p=n//100
	print(o , "+" , p)
print(o+p)