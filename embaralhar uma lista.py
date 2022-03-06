import random
names = input('digite o nome dos alunos')
lista = names.split()
random.shuffle(lista)
print('A classificação dos alunos é', lista)