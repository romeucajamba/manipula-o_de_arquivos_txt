try:
    arquivo = open("db.txt")
    print(arquivo.read())
except Exception as error:
    print("erro ao tentar fazer leitura do arquivo!! {}".format(error))

