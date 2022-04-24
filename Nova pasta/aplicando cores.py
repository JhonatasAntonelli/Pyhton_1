'''\033[(stilo);texto;backm
o stilo pode ser 0, 1(negrito), 4(italico), 7(inverte)
A cor do texto ´pde ser: 30(branco), 31(vermelho), 32(verde), 33(amarelo), 34(azul), 35(roxo), 36(azulpiscina), 37(cinza)
Back(fundo)40(branco), 41(vermelho), 42(verde), 43(amarelo), 44(azul), 45(roxo), 46(azulpiscina), 47(cinza)'''
print('\033[0;30mOlám mundo!\033[m')
print('\033[4;33mOlám mundo!\033[m')
print('\033[1;35;40mOlám mundo!\033[m')
print('\033[30;44mOlám mundo!\033[m')
print('\033[mOlám mundo!\033[m')
print('\033[7;30mOlám mundo!\033[m')

