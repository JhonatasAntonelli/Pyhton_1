import math
cat_opo = float(input('Digite o tamanho do cateto oposto'))
cat_adj = float(input('Digite o tamanho do cateto adjacente'))
hipo =math.sqrt((cat_adj**2) + (cat_opo**2))
print('A hipotenusa de um triangulo com cateto oposto {} e adjacente {} é de {:.2f}'.format(cat_opo, cat_adj, hipo))
