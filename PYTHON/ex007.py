#Crie um prgm que solicite o nome do aluno, suas 2 notas e calcule sua média
nome = input('Digite o nome do aluno: ')
n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
media=(n1 + n2) / 2
print('O nome do aluno é {} \nSuas notas foram {} e {} \nEntão sua média é = {:.1f}'.format(nome,n1,n2,media))