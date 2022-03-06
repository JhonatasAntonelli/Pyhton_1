import random
x = random.randint(0,5)
print('Para sair do jogo digite qualquer número acima de 5')
y = int(input('Tente adivinhar o número escolhido pelo computador, entre 0 e 5'))
while y!=x and y<=5:
    print('Que pena, você errou. Tente novamente')
    print ('O número escolhido pelo computador foi {}'.format(x))
    x = random.randint(0, 5)
    y = int(input('Tente adivinhar o número escolhido pelo computador'))
    if y==x:
        print('Parabéns! Você acertou')
        x = random.randint(0, 5)
        y = int(input('Tente adivinhar o número escolhido pelo computador'))
if y==x:
    print('Parabéns! Você acertou')
    x = random.randint(0, 5)
    y = int(input('Tente adivinhar o número escolhido pelo computador'))
if y>5:
    print('FIM')