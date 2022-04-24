x = float(input('Digite o comprimento da primeira reta'))
y = float(input('Digite o comprimento da segunda reta'))
z = float(input('Digite o comprimento da terceira reta'))
if x>y and x>z:
    tri = y + z
    if x > tri:
        print('Não é possivel formar um triângulo')
    else:
        print('É possivel formar um triângulo')
if y>z and y>x:
    tri = x + z
    if y > tri:
        print('Não é possivel formar um triângulo')
    else:
        print('É possivel formar um triângulo')
if z>y and z>x:
    tri = x + y
    if z > tri:
        print('Não é possivel formar um triângulo')
    else:
        print('É possivel formar um triângulo')
