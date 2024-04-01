#Crie um programa que leia quantos R$ tem uma pessoa e calcule qnts U$$ ela pode comprar
#Cotação dólar 01/04/2024 --> U$$ 1,00 = R$ 5,05
reais = float(input('Quantos reais você tem? '))
dolar = reais / 5.05
print('Com R$ {} eu consigo comprar U$$ {:.2f}'.format(reais,dolar))