#Aluguel de carros (Valor carro = 60 reais por dia) + (0.15 reais por km rodado)
qdia = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Digite a quantidade de KM rodados: '))
precoF = 60 * qdia + (0.15*km)
print('Fiquei com o carro durante {} dias.\nA quantidade de km rodados com o carro foi de {}km. Assim, o valor total a pagar é = R$ {}'.format(qdia, km, precoF))