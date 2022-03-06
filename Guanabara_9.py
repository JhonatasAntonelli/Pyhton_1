from math import sqrt, floor
num = int(input('Digite um número'))
raiz = sqrt(num)
print ('A raiz quadrada de {} é {:.3f}'.format(num, raiz))#utilizar {:.3f} para mostrar 3 digitos depois da virgula
print ('A raiz quadrada de {} é {}'.format(num, floor(raiz)))#utilizar o floor para arredondar para baixo
