#Um pgrm que leia a largura e a altura em M de uma parede e calcule sua área e a quantidade de tinta necessária para pintá-la (cada litro de tinta corresponde a 2m²)
largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
qtinta = area / 2
print('Sua parede tem altura = {}m e largura = {}m\nJá a área é = {}m² entãp irá ser preciso de {:.2f} litros de tinta'.format(altura, largura, area, qtinta))