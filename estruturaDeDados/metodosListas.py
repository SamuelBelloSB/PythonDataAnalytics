#   .append -> add elemento a lista
lista = []
lista.append(1)
lista.append("Python")
lista.append([40,50,30])
print("Método .append():")
print(lista)

#   .copy -> copia o elemento de uma lista
l1 = lista.copy()
print("Método .copy")
print(l1)
print(id(l1), id(lista))

#   .count -> conta os elementos de uma lista (suas repetições)
numeros = [1, 1, 1, 3, 2,4,3,2,9,1 ]
print("Método .count():")
print(f"O número 1 apareceu: {numeros.count(1)} vezes")
print(f"O número 2 apareceu: {numeros.count(2)} vezes")
print(f"O número 3 apareceu: {numeros.count(3)} vezes")

#   .extend -> junta objetos numa lista
lista.extend(numeros)
print(f"Método .extend(): \n{lista}")

#   .index  -> retorna o indice do objeto na lista
print("Método .index():")
print(lista.index("Python"))

#   .pop    -> remove o último objeto da lista ou o índice indicado
print(f"Método .pop(): \n{lista.pop()}")

#   .remove -> remove o objeto em questão da lista passando ele por argumento
print(f"Método .remove(): \n{lista[2].remove(40)}")
print(lista)

#   .clear -> limpa todos os elementos da lista
lista.clear()
print(lista)