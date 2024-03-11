###Lendo arquivos
archive = open('readFile.txt')
#print(archive.read())

###Escrever em arquivos
#myDb = open('db.txt', 'w')#Só adiciona 1 vez, e se tentar adicionar outra vez, ele vai subscrever
#writeText = str(input('Digite o que quiser: '))
#myDb.close()
#myDb.write(writeText)

# Adicionando mais textos ao arquivo
appendText = open('db.txt', 'a', encoding='cp1252') #Append, adicionar mais textos, sem subscrever
writeMytxt = str(input('Digita o texto: '))
appendText.write(writeMytxt)
appendText.close()