arq = open("02/saida/texto.txt","r")
texto = arq.read().lower().strip().split(" ")

word = []
for i in texto:
    if i not in word:
        word.append(i)
print(len(word))


arq.close()