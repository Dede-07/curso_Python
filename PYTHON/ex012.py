#Faça um algorítmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
preco = float(input('Digite o valor do produto: '))
novo = preco - (preco * 0.05)
print('O produto custa R$ {}\nCom 5% de desconto, o produto custará R$ {:.2f}'.format(preco, novo))