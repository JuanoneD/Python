# def soma(a,b):
#     soma = a + b
#     print(soma)
#     print("valor invalido")


# def subtração(a,b):
#     try:
#         soma = a - b
#         print (soma)
#     except ValueError:
#         print("valor invalido")

# def mult(a,b):
#     try:
#         soma = a * b
#         print (soma)
#     except ValueError:
#         print("valor invalido")
# def divisao(a,b):
#     try:
#         soma = a / b
#         print (soma)
#     except ZeroDivisionError:
#         print("Nâo pode ser dividido por zero")

# while 1:
#     try:
#         num1 = int(input("escreva 1 numero"))
#         num2 = int(input("escreva o segundo num"))
#         menu = int(input(" 1 = soma \n 2 = subtração \n 3 = mult \n 4 = divisao "))
#         if menu == 1:
#             soma(num1,num2)
#         elif menu == 2:
#             subtração(num1,num2)
#         elif menu == 3:
#             mult(num1,num2)
#         elif menu == 4:
#             divisao(num1,num2)
#         elif menu == 0:
#             break
#         else:
#             print("valor invalido")
#     except ValueError:
#         print("valor invalido")

import random

def listaword(a):
    i = 0
    with open("02/saida/words.txt") as arq:
        for linha in arq:
            i += 1 # i = i +1
            if i == a:
                return linha.strip().split(" ")

def embaralhar(words):
    tam = len(words)
    indiceWord = []
    while len(indiceWord) != tam:
        randola = random.randint(0,tam-1)
        if randola not in indiceWord:
            indiceWord.append(randola)
    return indiceWord
#main
while 1:
    try:
        dificuldade = int(input("escreva o nivel de dificuldade entre 1 a 3"))
        if dificuldade != 1 or dificuldade != 2 or dificuldade != 3:
            print("valor invalido")
        break
    except ValueError:
        print("valor invalido")
words = listaword(dificuldade)
key = words[random.randint(0,len(words)-1)].lower()
indiceWord = embaralhar(key)
for i in range(len(indiceWord)):
    print(key[indiceWord[i]],end="")
print("")
vida = 100
while vida >  0:
    chute = input("Escreva a palvara criptogradada ")
    if chute == key:
        print("voce acertou a palavra criptografada")
        break
    else:
        print("voce errou perdeu 20 de vida")
        vida -= 20
        print("vc tem {},de vida".format(vida))
if vida == 0:
    print("a palavra certa era ",key)
