#   As tuplas são imutáveis enquanto as listas são mutáveis

#   Declarações de tupla
frutas = ("laranja", "pera", "uva",)
letras = tuple("python")
numeros = tuple([1,2,3,4])
pais = ("Brasil",)

print(frutas)

#   Matrizes de tupla

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])       # -> [1, "a", 2]
print(matriz[0][0])    # -> 1
print(matriz[0][1])    # -> a
print(matriz[0][-1])   # -> 2
print(matriz[1][-1])   # -> 4

#   Métodos possíveis de utiliza na tupla
#   .index -> pegar o indice de um objeto |
#   .count -> contar elementos da tupla |
#   len -> informa o tamanho total de objetos da tupla