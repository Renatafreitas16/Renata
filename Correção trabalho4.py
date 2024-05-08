#3

def lista_de_compras():
    texto = input("Digite os itens da sua lista de compras separados por vírgula: ")
    lista = texto.split(',')

    contador = 1
    for itens in lista:
        print("item", contador,":", itens)
        contador+=1
