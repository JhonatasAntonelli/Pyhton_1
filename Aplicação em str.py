frase = 'Curso em Video Python'
print (frase)
print (frase[3])#imprime apenas o 3 caractere, lembrando que a contagem começa em 0 e o ultimo nã conta
print (frase[4:12])#imprime do 4 até o 11 caractere
print (frase[4:12:2])#imprime do 4-12 de 2 em 2
print (frase[:12:2])#imprime do primeiro até o 12 de 2 em 2
print (frase[::3])#imprime todos de 2 em 2
print (len(frase))#imprime o número de caracteres
print (frase.count('o'))#imprime a quantidade de vezes que o 'o' aparece
print (frase.count('o', 0,13))#imprime a quantidade de vezes que o 'o' aparece do primeiro até o 13 caractere
print (frase.find('deo'))#imprime o local quecomeça o 'deo'
print ('Curso' in frase)#imprime se encontrou o 'Curso' True ou False
print (frase.replace('Python', 'Android'))#troca a palavra Python por Android
print (frase.upper())#imprime tudo com letra maiuscula
print (frase.lower())#imprime tudo com letra minuscula
print (frase.capitalize())#imprime tudo com apenas a primeira letra da frase em maiuscula
print (frase.title())#imprime tudo com apenas a primeira letra de cada palavra em maiuscula
print (frase.strip())#imprime tudo sem os espaços do inicio e fim
print (frase.rstrip())#imprime tudo sem os espaços da direita
print (frase.split())#imprime tudo em lista de lista
print ('-'.join(frase))#imprime tudo com um - separando cada palavra
frase_separada = frase.split()
primeiro = frase_separada[0]
print (len(primeiro))