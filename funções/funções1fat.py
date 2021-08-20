def fat (n):
	fat = 1
	while n >1:
		fat= fat * n
		n= n-1
		
	return fat

n= int(input("n:	"))
print (fat(n))