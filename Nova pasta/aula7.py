nome = input('Qual o seu nome?')
print('prazer em te conhecer{:^20}!'.format(nome))# a expressão {:^20} faz com que seja impresso 20 espaços e o nome centralizado
print('prazer em te conhecer{:=<20}!'.format(nome))
print('prazer em te conhecer{:=^20}!'.format(nome))

n1 = int(input('Digite u valor'))
n2 = int(input('Digite u valor'))
s = n1 + n2
p = n1 * n2
d = n1 / n2
print('A soma é {},\n o produto é {}\n e a divisão é {:.3f}'.format(s, p, d),end=' ') # A expressão {:.3f} faz com que seja impresso apenas 3 caracteres depois da virgula e o ultimo é arredondado
print('usando ,=end ' ' você imprime tudo na mesma linha') # aquilo que esta entre aspas sera impresso, se deixar vazio ele imprime um espaço
print('A média de {} e {} é {:.1f}'.format(n1, n2, ((n1+n2)/2))