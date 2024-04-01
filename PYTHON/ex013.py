#faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
salario = float(input('Digite o salário do funcionário: '))
novos = salario + (salario * 0.15)
print('O salário antigo do funcionário era R$ {}\nCom 15% de aumento, o salário passa a ser R$ {:.2f}'.format(salario,novos))