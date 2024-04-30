palavra = "  pyTHon é DemAis  "

#   Maiúscula
print(palavra.upper())

#   Minúscula
print(palavra.lower())

#   Title - Primeira palavra em maiúsculo
print(palavra.title())

#   Eliminando espaços em branco
print(palavra.strip()) #    remove espaço de todos os lados
print(palavra.rstrip())#    remove espaço da direita
print(palavra.lstrip())#    remove espaço da esquerda

#   Junções e centralização
print(palavra.center(25, '#'))

print("/".join(palavra))