p1= float(input("nota da primeira prova:	"))
p2= float(input("nota da segunda prova:	"))
tr= float(input("nota do trabalho:	"))

r= p1*0.40
print("nota: %.2f"  %r)

s= p2*0.40
print("nota: %.2f"	%s)

t= tr*0.20
print("nota: %.2f"	%t)

w=r+s+t

print("nota final: %.2f" %w)