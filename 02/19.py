""" lista = [0,0,0,0,0,0,0,0,0,0]
for i in range (10):
    lista[i]=int(input("escreva o numero "))
tam = len(lista)
lista.sort()
print("tamanho da lista é ",tam,lista) """
""" t = ('jeff bezos','bill gates','warren buffet','bernard arnoult','amancio ortega','larry ellisomn','mark zuberg')
print(t)
print ('os 3 mais ricos são',t[:3])
print(' o mais rico é ',t[0])
 """
""" car = {'hamburguer': 10, 'hotdog':6.5, 'salada':4,'suco':4,'refri':4.5,'agua':2}
comi= input("comida desajada:")
bebi= input ("bebida desejada:")
tota = car[comi] + car[bebi]
print ("valor total: ",tota) """
""" num = 42
fla = 0
while fla != 1:
    sor=input("escreva seu palpite ")
    if sor.isdigit():
        if int(sor) == num:
            print("valor correto ")
            fla = 1
        else:
            print("valor incorreto ")
    else:
        print("digte um numero ") """
""" nas = int(input("escreva o ano de nascimento "))
ida = 2024 - nas
if ida < 16:
    print("não é permitido")
elif ida > 16 and ida < 18 or ida >70:
    print("facultativo")
else:
    print("voto obrigatorio") """
""" to = int(input("escreva o valor limite par soma"))
a = 0
s = 0
while a !=  to:
    a= a + 1
    s = a + s
print("soma total é ",s) """
num1 = int(input("escreva o  primeiro num "))
num2 = int (input("escreva o segundo num "))
while True:
    men = int(input ("digite \n 1- Soma \n 2- subtração \n 3- multiplicação \n 4- divisao \n 0- sair"))
    if men == 1:
         print("valor da soma: ",num1+num2)
    elif men == 2:
         print("valor da sub: ",num1-num2)
    elif men == 3:
         print("valor da mult: ",num1*num2)
    elif men == 4:
         print("valor da divisão",num1/num2)
    elif men == 0:
         break
    else:
         print("num invalido")