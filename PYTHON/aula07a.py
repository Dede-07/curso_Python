n1 = int(input('Digite um nº: '))
n2 = int(input('Digite outro nº: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end = ' ')
print('A divisao inteira {} e potência {}'.format(di, e))
