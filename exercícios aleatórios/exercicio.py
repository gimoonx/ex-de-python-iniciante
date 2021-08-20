n=int(input('n:	'))
q=n//100
r=n%100
s=q+r
x=s*s
if x==n:
	print('sim')
else:
	print('nao')