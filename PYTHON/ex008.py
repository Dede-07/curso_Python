#Crie um pgrm que leia um valor em Metros e depois mostre em cm e em mm
metros = float(input('Digite algum valor: '))
CM = metros * 100
MM = metros * 1000
print('O valor em metros é {}m \nO valor em Cm é {}cm \nO valor em Mm é {}mm'.format(metros, CM, MM))