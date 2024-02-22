import random
def criarlista(inferior,superior,tamanho):
    lista = []
    for i in range(tamanho):
        randola = random.randint(inferior,superior)
        lista.append(randola)
    return(lista)

def ordenarlista(lista,tamanho):
    j=1
    while j != 0:
        j = 0
        for i in range(tamanho - 1):
                if lista[i] > lista[i + 1]:
                    auxiliar = lista[i]
                    lista[i] = lista[i+1]
                    lista[i + 1] = auxiliar
                    j = i
    return(lista)


inferior = int(input("escreva o valor inferior"))
superior = int(input("escreva o valor superior"))
tamanho = int(input("escreva o tamanho"))
lista = criarlista(inferior,superior,tamanho)
print("lista aleatoria",lista)
lista = ordenarlista(lista,tamanho)
print("lista organizada",lista)



