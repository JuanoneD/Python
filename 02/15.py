#pal = input("escreva a palavra: \n")
#gra = pal.upper()
#print (gra[:3])

pal = input("escreva seu nome ocmpleto")
se = pal.split(' ')
p = se.count(' ')
p = p + 1
while p > 0:
    se[p].capitalize()
    p = p - 1
print(se)
