def tri (a, b, c):
	
	if (a+b<c) or (b+c<a) or (a+c<b):
		return False
		
	else:
		return True
		
a=float(input("lado a:	"))
b=float(input("lado b:	"))
c=float(input("lado c:	"))

print(tri (a, b, c))