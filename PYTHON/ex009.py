#Crie um pgrm que leia um nº e dê sua tabuada
n = int(input('Digite um nº para ter sua tabuada: '))
tabuada = 1
while (tabuada < 11):
    print('{} * {} = {}' .format(n, tabuada, n*tabuada))
    tabuada = tabuada + 1