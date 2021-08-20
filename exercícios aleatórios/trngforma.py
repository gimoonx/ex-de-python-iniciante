a= int(input("primeiro lado:	"))
b= int(input("segundo lado:	"))
c= int(input("terceiro lado:	"))

if (a+b<c) or (a+c<b) or (b+c<a):
	print ("não formam um triângulo")
elif (a==b==c) or (a==b) or (a==c) or (b==c):
	print ("formam")
else:
	print ("formam")