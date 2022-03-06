from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo'))
cos = cos(radians(angulo))
sen = sin(radians(angulo))
tan = tan(radians(angulo))
print ('O consseno do ângulo é {}, o seno é {} e a tangente {}'.format(cos, sen, tan))