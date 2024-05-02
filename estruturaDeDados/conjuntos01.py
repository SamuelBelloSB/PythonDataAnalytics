#   Conjuntos são uma coleção de objetos únicos.

""" print(set([1,2,3,1,3,4])) -> {1, 2, 3, 4}
print(set("abacaxi")) -> {'b', 'a', 'c', 'x', 'i'}   
A Ordem dos elementos é aleatória.
"""

carros = set(("palio", "gol", "celta", "palio",))
print(carros)

#   Pode-se declarar conjuntos com {} | set() == {}
linguagem = {"python", "java", "javascript", "php", "java"}
print(linguagem)

""" 
Os conjuntos não suportam indexação e nem fatiamento,
caso precise acessar os valores é necessário converter
o conjunto para lista!
"""

numeros = {1,2,3,2}
numeros = list(numeros)
print(numeros[-1])

#   Utilizando for
for carro in carros:
    print(carro)
    
#   Função enumerate
for indice, carro in enumerate(carros):
    print(f"índice {indice}: {carro}")