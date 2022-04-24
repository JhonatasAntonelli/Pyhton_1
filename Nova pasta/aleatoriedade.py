import random
names = input('digite o nome dos alunos')
lista = names.split()
x = random.randint(0,3)
print('O aluno escolhido foi o aluno', lista[x])