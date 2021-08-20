print("Digite a primeira data")
d = int(input("dia:	"))
m = int(input("mês:	"))
a = int(input("ano:	"))

print("Digite a segunda data")
y =int(input("dia:	"))
o =int(input("mês:	"))
u =int(input("ano:	"))

if a>u:
    print("Esta data é mais recente",d,"/", m,"/", a)
elif u>a:
    print("Esta data é mais recente",y,"/",o,"/",u)
elif m>o:
    print("Esta data é mais recente",d,"/", m,"/", a)
elif o>m:
    print("Esta data é mais recente",y,"/",o,"/",u) 
elif d>y:
    print("Esta data é mais recente",d,"/", m,"/", a)
elif y>d:
    print("Esta data é mais recente",y,"/",o,"/",u)
else:
    print("São a mesma data")