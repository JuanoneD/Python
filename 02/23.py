""" def escrevernota():
    arq = open("02/saida/notas.txt","a")
    nota=input("escreva o nome e notas do 1,2,3 trimestre separado por vigula ")
    arq.write(nota + "\n")

def vernota():
    arqpro = open ("02/saida/notas_processadas.txt","w")
    maiornota = 0
    with open ("02/saida/notas.txt") as arq:
        for linha in arq:
            linha = linha.strip()
            linha = linha.split(",")
            media = (int(linha[1]) + int(linha[2])+int(linha[3]))/3
            if media > 6:
                apro = "aprovado"
            else:
                apro = "reprovado"
            if media > maiornota:
                maiornota = media
                nome = linha[0]
            texto = str(linha[0]) +","+ str(media) +","+ str(apro)
            arqpro.write(texto + "\n")
        arqpro.close()
    arq = open("02/saida/notas_processadas.txt","r")
    print("maior nota é: ",nome, maiornota)
    print(arq.read())
    arqpro.close()


while True:
    menu = int(input(" 1: Cadastrar notas \n 2: Visualizar notas \n 0: Sair "))
    if menu == 1:
        escrevernota()
    elif menu == 2:
        vernota()
    elif menu == 0:
        break
    else:
        print("valor invalido ") """

arq = open("02/saida/arq.txt","r")
texto = arq.read()
texto = texto.strip()
texto = texto.lower()
texto = texto.split(" ")
lista = []
for i in len(texto):
    for j in len(texto):
        count = 0
        if texto[i] == texto[j]:
            count = count + 1
        if count > 1:
            lista.append 
            
