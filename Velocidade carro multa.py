x = int(input('Digite a velocidade do carro'))
if x>80:
    print('Você utrapassou a velocidade llimite e vai levar multa')
    multa = (x-80)*7
    print('A sua multa vai ser de {}'.format(multa))
else:
    print('Você não ultrapassou a velocidade e não vai levar multa')
