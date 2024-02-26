""" for i in range(0,31,1):
    if i % 2 == 0:
        print(i)
 """
""" x = int(input("escreva o valor do tab "))
if x > 0:
    for i in range(0,x,1):
        for j in range (0,x,1):
            print("x", end=' ')
        print("") """

""" fat = int(input("escreva o num de fat"))
z = 0
y = 1
print (z)
print (y)
for i in range(0,fat-2,2):
    z = z + y
    print(z)
    y = z + y
    print (y)
 """

""" x = int(input("escreva um num "))
lis = []
for i in range (1,x + 1,1):
    if x % i == 0:
        lis.append(i)
print(lis)

if len(lis) > 2:
    print("não é primo")
else:
    print("é primo") """

""" import random
fla = 0
op = {"impar":0,"par":1}
while True:
    es = input(" escreva par ou impar ").lower()
    x = int(input("escreva o valor para jogar "))
    if x < 11 and x > -1:
        y = random.randint(0,10)
        print("computador escolheu ",y)
        if (x + y) % 2 == 0 and op[es] == 1:
            print("Resultado par jogador ganhou ")
            fla += 1
        elif (x + y) % 2 != 0 and op[es] == 0:
            print("Resultado Impar jogador ganhou ")
            fla += 1
        else:
            print("jogador perdeu ")
            print("Numero de vitorias",fla)
            break """

""" import time
def contagem():
    for i in range (3,0,-1):
        print(i)
        time.sleep(1)

contagem() """
""" 
import random
fla = 0
op = {"impar":0,"par":1}
while True:
    es = input(" escreva par ou impar ").lower()
    x = int(input("escreva o valor para jogar "))
    if x < 11 and x > -1:
        y = random.randint(0,10)
        print("computador escolheu ",y)
        if (x + y) % 2 == 0 and op[es] == 1 or (x + y) % 2 != 0 and op[es] == 0:
            print("Jogador ganhou ")
            fla += 1
        else:
            print("jogador perdeu ")
            print("Numero de vitorias",fla)
            break """


