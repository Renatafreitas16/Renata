#print("olá","renata",sep="-")

#print("olá","renata",end="!\n")

#print("16", "12", "2003", sep="/")

#print("nome", "sobrenome", "email", sep="; ")

#print("Loading", end=" ")
#print("[OK]")

#nome = input("Digite seu nome: ")
#print("Olá", nome)

#itens = input("Digite itens separados por vírgula: ").split(',')
#print("Itens:", itens)

#idade = int(input("Digite sua idade: "))
#print("Daqui a cinco anos, você terá", idade + 5, "anos.")

#altura = float(input("Digite sua altura em metros: "))
#print("Sua altura é", altura, "metros.")

#print("Digite números para adicionar à lista (digite 'done' para terminar):")
#numeros = []
#while True:
    #entrada = input()
    #if entrada.lower() == 'done':
        #break
    #else:
        #numeros.append(int(entrada))
#print("Números coletados:", numeros)

#1
def seus_dados():
    print("nome; renata "," idade:20 anos "," cidade: rio de janeiro",sep="-",end="!\n")

#2
def dois_numeros():
    num1 = float(input("digite um numero: "))
    num2 = float(input("agora digite outro numero: "))
    print(num1+num2)

#3
def lista_de_compras():
    itens = input("Digite os itens da sua lista de compras separados por vírgula: ").split(',')
    print("itens:", itens)

#4
print("conversor de celcius para fahrenheit")

celcius = float(input("digite a temperatura em celsius: "))
fahrenheit=input((9/5)*celcius +32)

#5

print("Digite nomes para adicionar à lista (digite 'sair' para terminar):")
nomes = []
while True:
    entrada = input()
    if entrada.lower() == 'sair':
        break
    else:
        nomes.append(int(entrada))
print("nomes coletados:", numeros)
