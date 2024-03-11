#Manipulando arquivo de forma dinâmica!!

list = []
manipulation = []

with open('db.txt') as arquivo:
    ######## Lendo arquivo linha por linha #####
    print(arquivo.readLine())
    list = arquivo.readlines()
    print(list)

    ############### Fatiando strings ##########

    manipulation = arquivo.readlines().split()

    print(manipulation[::2])
    print(manipulation[1::2])

    for lista in manipulation:
        print(lista)