def soma(a,b):
    return a + b

def quadrado(a):
    return a**2

def hipotenusa(cateto1,cateto2):
    return soma(quadrado(cateto1),quadrado(cateto2))**(1/2)

def simples(cor):
    if cor == 'azul':
        return 'a cor do capitão america'

def medio(cor):
    if cor == 'verde':
        return 'a cor do hulk'
    else:
        return 'escolhe outra'

def completo(cor):
    if cor == 'amarelo':
        return 'a cor do sol'
    elif cor == 'vemelho':
        return 'a cor do homem de ferro'
    elif cor == 'roxo':
        return 'a cor do açaí'
    else:
        return 'bora, escolhe outro'

numeros = [1,2,3,4,5]
print(numeros[0])
print (numeros[-1])
numeros[0] = 10
print(numeros)

#contar de 1 a 9#

contador = 0
while contador < 10:
    print(contador)
    contador += 1

#contar de novo de 1 até 9#

for i in range(10):
    print(i)


#agora vai uma lista diferente#
    
for item in [1,45,78,'a',[3,5]]:
    print(item)

#meu nome#
    
for letra in 'renata':
    print(letra)

#triangulo

for i in range(6):
    print((i + 1) * "*")






