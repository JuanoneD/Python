""" import time
def contador(inicio,fim,passos):
    if passos > 0:
        for i in range(inicio,fim+1,passos):
            time.sleep(1)
            print(i)
    else:
        for i in range(inicio,fim-1,passos):
            time.sleep(1)
            print(i)
    

inicio = int(input("escreva o valor de incio "))
fim = int(input("escreva o valor fim "))

if inicio >= 1 and fim <= 20 and fim > inicio:
    print("1 a 20")
    passos = 1
elif inicio <= 20 and fim >= 0 and inicio > fim:
    print("20 a 0")
    passos = -2
elif inicio <= 96 and fim <= 52 and inicio > fim:
    print("96 a 52")
    passos = -2
elif inicio >= 3 and fim <= 41 and fim > inicio:
    print("3 a 40")
    passos = 1
elif inicio <= 75 and fim >= 15 and inicio > fim:
    print("75 a 15")
    passos = -5
elif inicio <= 390 and fim >= 39 and inicio > fim:
    print("390 a 39")
    passos= -10
else:
    passos = int(input("escreva o valor desejado para passos"))

contador(inicio,fim,passos)
 """

""" def oparacoes(num):
    fatorial = num
    for i in range(1,num + 1,1):
        fatorial = fatorial * i;
    inverso = 1 / num
    quadrado = num ** 23
    raiz = num ** 0.5
    return{"raiz quadrada":raiz,"quadrado":quadrado,"inverso":inverso,"fatorial":fatorial}

while True:
    num = int(input("escreva um numero ou menor que 0 para sair"))
    if num <= 0:
        break
    resultados = oparacoes(num)
    print(resultados)
 """
import random

def criar_lista(a,b,c):
    listas = []
    for i in range(c):
        randola = random.randint(a,b)
        listas.append(randola)
        print("asdasdasd")
        return (listas)

def ordenar(lista,tam):
    for i in range(tam):
        for j in range(tam):
            if lista[j+1] < lista[j]:
                sup = lista[j+1]
                lista[j] = lista[j+1]
                lista[j] = sup
    return(lista)

inferior = int(input("escreva o limete inferior"))
superior = int (input("escreva o valor superior"))
tamanho = int(input("tamanho da lista"))
lista = criar_lista(inferior,superior,tamanho)
print(lista)    

# Python é paia 
